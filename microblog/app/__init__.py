#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir
__author__ = 'Liu Lixiang'

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u'请先登录系统'
open_id = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
