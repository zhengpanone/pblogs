=============================
20.2 Request and Response
=============================

------------------------------
1 获取请求数据，及响应
------------------------------
    -Request
            -request.form   # POST请求的数据
            -request.args   # GET 请求数据，不是完全意义上的dict ，通过 .to_dict 可以转换成字典
            -request.querystring    # GET 请求，bytes 形式的
    -Response
            -return render_tempalte()
            -return redirect()
            -return ""
            v = make_response(返回值)   # 可以把返回值包在函数里，再通过 .set_cookie 绑定cookie等
    -session
            - 存在浏览器上，并且是加密的
            - 依赖于：secret_key

-----------------------------------
2 flask 中获取URL后面的参数
-----------------------------------

from urllib.parse import urlencode,quote,unquote
GET 请求：
URL为：http://127.0.0.1:5000/login?name=%27%E8%83%A1%E5%86%B2%27&nid=2

::

 from urllib.parse import urlencode,quote,unquote

 def login():
 if request.method == 'GET':
        s1 = request.args
        s2 = request.args.to_dict()
        s3 = urlencode(s1)
        s4 = urlencode(s2)
        s5 = unquote(s3)
        s6 = unquote(s4)
        s7 = quote("胡冲")
        print('s1',s1)
        print('s2',s2)
        print('s3',s3)
        print('s4',s4)
        print('s5',s5)
        print('s6',s6)
        print('s7',s7)

        return render_tempalte('login.html')

 >>>s1 ImmutableMultiDict([('name', "'胡冲'"), ('nid', '2')])
 s2 {'name': "'胡冲'", 'nid': '2'}
 s3 name=%27%E8%83%A1%E5%86%B2%27&nid=2
 s4 name=%27%E8%83%A1%E5%86%B2%27&nid=2
 s5 name='胡冲'&nid=2
 s6 name='胡冲'&nid=2
 s7 %E8%83%A1%E5%86%B2



请求与响应

::

 from flask import Flask
 from flask import request
 from flask import render_template
 from flask import redirect
 from flask import make_response

    app = Flask(__name__)


    @app.route('/login.html', methods=['GET', "POST"])
    def login():

        # 请求相关信息
        # request.method
        # request.args
        # request.form
        # request.values
        # request.cookies
        # request.headers
        # request.path
        # request.full_path
        # request.script_root
        # request.url
        # request.base_url
        # request.url_root
        # request.host_url
        # request.host
        # request.files
        # obj = request.files['the_file_name']
        # obj.save('/var/www/uploads/' + secure_filename(f.filename))

        # 响应相关信息
        # return "字符串"
        # return render_template('html模板路径',**{})
        # return redirect('/index.html')

        # response = make_response(render_template('index.html'))
        # response是flask.wrappers.Response类型
        # response.delete_cookie('key')
        # response.set_cookie('key', 'value')
        # response.headers['X-Something'] = 'A value'
        # return response


        return "内容"

    if __name__ == '__main__':
        app.run()



::

 from flask import Flask,url_for,request,redirect,render_template,jsonify,make_response
 from urllib.parse import urlencode,quote,unquote
 app = Flask(__name__)

 @app.route('/index',endpoint='xx')
 def index():
    from werkzeug.datastructures import ImmutableMultiDict
　　
    # get_data = request.args
    # get_dict = get_data.to_dict()
    # get_dict['xx'] = '18'
    # url = urlencode(get_dict)
    # print(url)
　　
    # print(request.query_string)
    # print(request.args)
　　
    # val = "%E6%8A%8A%E5%87%A0%E4%B8%AA"
    # print(unquote(val))   #把上面这样的数据转换成中文
    #
    # return "Index"

    # return "Index"
    # return redirect()
    # return render_template()
    # return jsonify(name='alex',age='18')  #相当于JsonResponse
　　
    response = make_response('xxxxx')   ##如果是返回更多的值，cookie，headers，或者其他的就可用它
    response.headers['xxx'] = '123123'
    return response


 if __name__ == '__main__':
    # app.__call__
    app.run()