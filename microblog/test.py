#!flaskmac/bin/python
# -*- coding:utf-8 -*-

__author__ = 'liulixiang'

if __name__ == '__main__':
    from app import models, db
    u = models.User(nickname=u'刘理想', email='liulixiang1988@gmail.com', role=models.ROLE_USER)
    db.session.add(u)
    db.session.commit()
    u = models.User(nickname=u'龙珑', email='303875267@qq.com', role=models.ROLE_ADMIN)
    db.session.add(u)
    db.session.commit()
    users = models.User.query.all()
    print users, type(users)
    for user in users:
        print user.id, user.nickname, user.email
    user = models.User.query.get(1)
    print user.id, user.nickname
    import datetime
    post = models.Post(body=u'理想和龙珑，好好生活', timestamp=datetime.datetime.utcnow(), author=user)
    db.session.add(post)
    db.session.commit()
    p = user.posts.all()
    for i in p:
        print i.id, i.body, i.timestamp, i.author.nickname

    for user in users:
        db.session.delete(user)

    posts = models.Post.query.all()
    for post in posts:
        db.session.delete(post)
    db.session.commit()