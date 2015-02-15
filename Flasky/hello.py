#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'liulixiang'
from datetime import datetime

from flask import Flask, render_template, redirect, url_for, session, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'akoejanfaejajenoi193y1$ajfeHjiemadeiagnba*kjie'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField(u'你的名字是什么？')
    submit = SubmitField(u'提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash(u'看来你改名字了~')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'), current_time = datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_note_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    manager.run()
