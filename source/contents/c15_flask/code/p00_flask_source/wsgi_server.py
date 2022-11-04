# 1.可调用对象是一个函数
def application(environ, start_response):
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']

    HTTP response code and message
    status = '200 OK'

    # 应答头部是一个列表，每对键值都必须是一个tuble
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]

    # 调用服务器程序提供的start_response，填入两个参数
    start_response(status, response_headers)

    # 返回必须是iterable
    return [response_body]


class AppClass:
    '''这里的可调用对象就是 AppClass 的实例，使用方法类似于：
        app = AppClass()
        for result in app(environ, start_response):
            do_somthing(result)
    '''

    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'test/plain')]
        self.start(status, response_headers)
