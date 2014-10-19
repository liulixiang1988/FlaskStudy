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

###1.2 变量

Jinja2识别任意类型的变量，甚至是一些复杂的类型，比如列表、字典和对象。下面是一些常见的用法

```
<p>从字典中取值:{{ mydict['key'] }}</p>

<p>从列表中取值：{{ mylist[3] }}</p>

<p>使用一个变量从列表中取值：{{ mylist[myintvar] }}</p>

<p>对象方法返回的值：{{ myobj.somemethod() }}</p>
```

变量可以使用*过滤器*进行修改，使用`|`调用过滤器，比如下面的例子是让首字母大写：

```
Hello, {{ name|capitalize }}
```

下表列出了Jinja2中常见的过滤器：

过滤器|解释
-----|----
safe|不对值进行escape
capitalize|首字母大写
lower|转换小写
upper|转换大写
title|转换每个单词的首字母为大写
trim|去除前后的空白
striptags|在渲染前移除值中的HTML中的tag

