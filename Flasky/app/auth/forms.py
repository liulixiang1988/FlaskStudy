# -*- coding:utf-8 -*-
__author__ = 'liulixiang'

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'保持登录')
    submit = SubmitField(u'登录')


class RegistrationForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(u'用户名', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                                                     0, u'用户名必须是字符串'
                                                                                        u'、数字、点或者下划线')])
    password = PasswordField(u'密码', validators=[DataRequired(), EqualTo('password2', message=u'两次输入的密码不一致')])
    password2 = PasswordField(u'再次输入密码', validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已经被使用了')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已经被使用了')


class ChangePasswordForm(Form):
    current_password = PasswordField(u'原有密码', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired(), EqualTo('password2', message=u'两次输入的密码不一致')])
    password2 = PasswordField(u'再次输入密码', validators=[DataRequired()])
    submit = SubmitField(u'更改密码')


class ResetPasswordRequestForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField(u'提交')


class ResetPasswordForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'新密码', validators=[DataRequired(), EqualTo('password2', message=u'两次输入的密码不一致')])
    password2 = PasswordField(u'再次输入密码', validators=[DataRequired()])
    submit = SubmitField(u'重置密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError(u'该邮箱没有注册过账户')


class ChangeEmailRequestForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱已经被使用')