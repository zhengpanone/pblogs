from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "sdsfdsgdfgdfgfh"   # 设置session时，必须要加盐，否则报错


def wrapper(func):
    def inner(*args, **kwargs):
        if not session.get("user_info"):
            return redirect("/login")
        ret = func(*args, **kwargs)
        return ret
    return inner


@app.route("/login", methods=["GET", "POST"])  # 指定该路由可接收的请求方式，默认为GET
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # print(request.values)   #这个里面什么都有，相当于body
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "haiyan" and password == "123":
            session["user_info"] = username
            # session.pop("user_info")  #删除session
            return redirect("/index")
        else:
            # return render_template("login.html",**{"msg":"用户名或密码错误"})
            return render_template("login.html", msg="用户名或者密码错误")


@app.route("/index", methods=["GET", "POST"])
@wrapper  # 自己定义装饰器时，必须放在路由的装饰器下面
def index():
    # if not session.get("user_info"):
    #     return redirect("/login")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
