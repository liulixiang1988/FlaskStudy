# -*- coding:utf-8 -*-
__author__ = 'liulixiang'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp
from ..models import Role, User


class NameForm(Form):
    name = StringField(u'你的名字是什么？', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class EditProfileForm(Form):
    name = StringField(u'昵称', validators=[Length(0, 64)])
    location = StringField(u'地址', validators=[Length(0, 64)])
    about_me = TextAreaField(u'关于我')
    submit = SubmitField(u'保存')


class EditProfileAdminForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(0, 64), Email()])
    username = StringField(u'用户名', validators=[DataRequired(), Length(0, 64),
                                               Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                      0, u'用户名必须是由字母、数字、点和下划线组成')])
    confirmed = BooleanField(u'帐号确认')
    role = SelectField(u'角色', coerce=int)
    name = StringField(u'昵称', validators=[Length(0, 64)])
    location = StringField(u'地址', validators=[Length(0, 64)])
    about_me = TextAreaField(u'关于我')
    submit = SubmitField(u'保存')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已经注册过了')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已经被使用')
