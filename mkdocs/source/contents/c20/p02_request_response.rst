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
2 flask 中获取URL后面的参数（from urllib.parse import urlencode,quote,unquote）
-----------------------------------
    
GET 请求：
URL为：http://127.0.0.1:5000/login?name=%27%E8%83%A1%E5%86%B2%27&nid=2

::

 from urllib.parse import urlencode,quote,unquote

 def login():
 if request.method == 'GET':
        s1 = request.args
        s2 = request.args.to_dict()
        

