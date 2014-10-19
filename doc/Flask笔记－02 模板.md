title:Flask笔记－02 模板
date:2014-10-19 22:40
category:Python
tags:Flask, Flask笔记
author:刘理想

##1. Jinja2模板引擎

###1.1 渲染模板

默认情况下，Flask查找templates子目录下的模板。

我们添加两个模板文件：

*templates/index.html*

```
<h1>hello world!</h1>
```

*templates/user.html*

```
<h1>hello {{ name }}!</h1>
```

渲染使用`render_template`，那么渲染文件如下:

*hello.py*

```python
from flask import Flask, render_template
#...

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
```