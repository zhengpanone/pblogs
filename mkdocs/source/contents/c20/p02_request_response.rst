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

