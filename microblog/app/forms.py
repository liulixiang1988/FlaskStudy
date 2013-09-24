# -*- coding: utf-8 -*-
__author__ = 'liulixiang'

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
from models import User


class LoginForm(Form):
    openid = TextField('openid', validators=[Required(message=u'请输入openid')])
    remember_me = BooleanField(u"remember_me", default=False)


class EditForm(Form):
    nickname = TextField('nickname', validators=[Required(message=u'请输入用户名')])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user is not None:
            self.nickname.errors.append(u'用户名已经存在')
            return False
        return True

