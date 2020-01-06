import tornado.web  # web框架模块
import tornado.ioloop # 核心IO循环模块


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def get(self):
        """get请求"""
        self.write("Hello Tornado!")


if __name__ == "__main__":
    app = tornado.web.Application([(r'/', IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
