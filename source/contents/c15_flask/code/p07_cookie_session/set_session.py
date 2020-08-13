from flask import Flask, url_for, session

app = Flask(__name__)
app.secret_key = "sdsfdgdgdgd"
app.config['SESSION_COOKIE_NAME'] = 'session_lvning'  # 设置session的名字


@app.route('/index/')
def index(nid):
    # session本质上操作的是字典， 所有对session操作的方法与字典方法相同
    # session的原理：如果下一次访问的时候带着随机字符串，会把session里面对应的
    # 值拿到内存，假设session保存在数据库，
    # 每执行一次链接一次数据库，每次都要时时更新的话，会非常损耗数据库的效率
    session["xxx"] = 123
    session["xxx2"] = 123
    session["xxx3"] = 123
    session["xxx4"] = 123
    del session["xxx2"]  # 在这删除了，真正存储的时候是没有xxx2的
    return "ddsf"


if __name__ == '__main__':
    app.run()
