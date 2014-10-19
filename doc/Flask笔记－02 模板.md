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

###1.3 控制结构

1. 条件

```
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, stranger!
{% endif %}
```

2. 循环

```
<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```

3. 宏

类似Python代码，比如

```
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>
```

为了让宏更有用，可以把它们保存到一个文件里，然后`import`到模板里：

```
{% import 'macro.html' as macros %}

<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>
```

4. 导入重复多次的代码

可以把多次使用的代码段保存到一个单独的文件，然后在需要的地方导入它们。

```
{% include 'common.html' %}
```

5. 模板继承

创建一个基础模板*base.html*:

```
<html>
<head>
    {% block head %}
        <title>{% block title %}{% endblock %} - 我的应用</title>
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

上面这个模板有3个block，*head*, *title*, *body*，而且，*title*块还在*head*块内。

下面是子模板:

```
{% extends "base.html" %}

{% block title %}首页{% endblock %}

{% block head %}
    {{ super() }}
    <style type="text/css"></style>
{% endblock %}

{% block body %}
<h1>你好，世界！</h1>
{% endblock %}
```

注意，首先要声明继承的文件；第二个需要注意的是如果在保留块内容的基础上增加一些新的内容，可以使用`super()`方法，它是用来保留原来块内容的。

##2. 使用Flask-Bootstrap集成twitter bootstrap

