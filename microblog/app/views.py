# -*- coding: utf-8 -*-
__author__ = 'Liu Lixiang'
from flask import render_template, redirect, g, url_for, session, flash, request
from flask.ext.login import login_user, current_user, login_required, logout_user
from datetime import datetime
from app import app, db, login_manager, open_id
from app.models import User, ROLE_USER
from .forms import LoginForm, EditForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': u'在路上的理想'},
            'body': u'今天是个好日子！'
        },
        {
            'author': {'nickname': u'福宝'},
            'body': u'我爱我的理想'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@open_id.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return open_id.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template("login.html",
                           title=u"登录",
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@open_id.after_login
def after_login(resp):
    if resp.email is None or resp.email == '':
        flash(u'登录不正确，请再试一次。')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == '':
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email, role=ROLE_USER)
        db.session.add(user)
        db.session.commit()
        #添加自己为关注者
        db.session.add(user.follow(user))
        db.session.commit()
    remember_me = False
    if 'remeber_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/follow/<nickname>')
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash(u'没有找到' + nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash(u'不能follow自己啊亲')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.follow(user)
    if u is None:
        flash(u'无法关注' + nickname)
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash(u'关注成功！')
    return redirect(url_for('user', nickname=nickname))


@app.route('/unfollow/<nickname>')
def unfollow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash(nickname+u'不存在')
        return redirect(url_for('index'))
    if user == g.user:
        flash(u'不能取消对自己的关注')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.unfollow(user)
    if u is None:
        flash(u'无法取消关注' + nickname)
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash(u'成功取消关注'+nickname)
    return redirect(url_for('user', nickname=nickname))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    """

    :param nickname:
    :return:
    """
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash(u'没有找到' + nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': u'好好奋斗！为老婆创造更好的生活！'},
        {'author': user, 'body': u'你必须很努力，才能看起来毫不费力！'}
    ]
    return render_template('user.html',
                           title=u'用户' + nickname,
                           user=user,
                           posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash(u'更新已经成功保存！')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html',
                           title=u'用户信息更新',
                           form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500