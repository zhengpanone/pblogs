from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 定义转换的类
class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """路由匹配时匹配成功后传递给视图函数中参数的值"""

        return int(value)

    def to_url(self, value):
        """使用url_for 反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数"""
        val = super(RegexConverter, self).to_url(value)
        return val


# 添加到converts中
app.url_map.converters['regex'] = RegexConverter


# 进行使用
@app.route('/index/<regex("\d+"):nid>', endpoint='xx')
def index(nid):
    url_for('xx', nid=123)
    return "Index"


if __name__ == '__main__':
    app.run()
