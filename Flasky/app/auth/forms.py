# -*- coding:utf-8 -*-
__author__ = 'liulixiang'

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'保持登录')
    submit = SubmitField(u'登录')
