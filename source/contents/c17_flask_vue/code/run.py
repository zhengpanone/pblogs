# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/9/4 17:21
"""

# import lib

from flask import Flask, render_template

app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
