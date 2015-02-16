# -*- coding:utf-8 -*-
__author__ = 'liulixiang'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(Form):
    name = StringField(u'你的名字是什么？', validators=[DataRequired()])
    submit = SubmitField(u'提交')