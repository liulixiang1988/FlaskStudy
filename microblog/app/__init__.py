#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir, ADMINS, MAIL_SERVER, MAIL_POST, MAIL_USERNAME, MAIL_PASSWORD

__author__ = 'Liu Lixiang'

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u'请先登录系统'
open_id = OpenID(app, os.path.join(basedir, 'tmp'))

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler, RotatingFileHandler
    #credentials = None
    #if MAIL_USERNAME or MAIL_PASSWORD:
    #    credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    #mail_handler = SMTPHandler((MAIL_SERVER, MAIL_POST), 'no-reply@'+MAIL_SERVER, ADMINS, u'微博出错', credentials)
    #mail_handler.setLevel(logging.ERROR)
    #app.logger.addHandler(mail_handler)
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1*1024*1024, 10)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info(u'microblog启动')

from app import views, models
