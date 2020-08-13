from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    return '测试主页面'


movies = [1, 2, 3, 4, 5]


@app.route('/movie/<int:num>/')
def movie(num):
    if num in movies:
        return '电影 {} 的详细信息为：...... '.format(num)
    abort(404)  # 自己编写的404页面会显示在这里


@app.errorhandler(404)  # 404页面钩子
def page_404(er):  # 参数是原始的404页面提示信息
    print(er)
    return '这是统一的错误页面', 404, {}  # 返回自己编写的404页面信息


print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
