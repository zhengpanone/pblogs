=========================
15.7 Session
=========================

除请求对象之外，还有一个 session 对象。它允许你在不同请求间存储特定用户的信息。它是在 Cookies 的基础上实现的，并且对 Cookies 进行密钥签名要使用会话，你需要设置一个密钥。
设置：session['username'] ＝ 'xxx'
删除：session.pop('username', None)

::

 from flask import Flask,url_for,session

 app = Flask(__name__)
 app.secret_key = "sdsfdgdgdgd"
 app.config['SESSION_COOKIE_NAME'] = 'session_lvning'  #设置session的名字

 @app.route('/index/')
 def index(nid):
    #session本质上操作的是字典， 所有对session操作的方法与字典方法相同
    #session的原理：如果下一次访问的时候带着随机字符串，会把session里面对应的
    # 值拿到内存，假设session保存在数据库，每执行一次链接一次数据库，每次都要时时更新的话，会非常损耗数据库的效率
    session["xxx"] = 123
    session["xxx2"] = 123
    session["xxx3"] = 123
    session["xxx4"] = 123
    del session["xxx2"]  #在这删除了，真正存储的时候是没有xxx2的
    return "ddsf"

 if __name__ == '__main__':
    app.run()

关于session的配置
--------------------------------

app.config['SESSION_COOKIE_NAME'] = 'session_lvning'

::

 - session超时时间如何设置？      'PERMANENT_SESSION_LIFETIME':           timedelta(days=31)
 以下是跟session相关的配置文件
 """
            'SESSION_COOKIE_NAME':                  'session',
            'SESSION_COOKIE_DOMAIN':                None,
            'SESSION_COOKIE_PATH':                  None,
            'SESSION_COOKIE_HTTPONLY':              True,
            'SESSION_COOKIE_SECURE':                False,
            'SESSION_REFRESH_EACH_REQUEST':         True,  #是否每次都跟新
            'PERMANENT_SESSION_LIFETIME':           timedelta(days=31)
 """

基本使用

::

 from flask import Flask, session, redirect, url_for, escape, request
 
 app = Flask(__name__)
 
 @app.route('/')
 def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'
 
 @app.route('/login', methods=['GET', 'POST'])
 def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
 
 @app.route('/logout')
 def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
 
 # set the secret key.  keep this really secret:
 app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

自定义session

::

 pip3 install Flask-Session
        
        run.py
            from flask import Flask
            from flask import session
            from pro_flask.utils.session import MySessionInterface
            app = Flask(__name__)

            app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
            app.session_interface = MySessionInterface()

            @app.route('/login.html', methods=['GET', "POST"])
            def login():
                print(session)
                session['user1'] = 'alex'
                session['user2'] = 'alex'
                del session['user2']

                return "内容"

            if __name__ == '__main__':
                app.run()

        session.py
            #!/usr/bin/env python
            # -*- coding:utf-8 -*-
            import uuid
            import json
            from flask.sessions import SessionInterface
            from flask.sessions import SessionMixin
            from itsdangerous import Signer, BadSignature, want_bytes


            class MySession(dict, SessionMixin):
                def __init__(self, initial=None, sid=None):
                    self.sid = sid
                    self.initial = initial
                    super(MySession, self).__init__(initial or ())


                def __setitem__(self, key, value):
                    super(MySession, self).__setitem__(key, value)

                def __getitem__(self, item):
                    return super(MySession, self).__getitem__(item)

                def __delitem__(self, key):
                    super(MySession, self).__delitem__(key)



            class MySessionInterface(SessionInterface):
                session_class = MySession
                container = {}

                def __init__(self):
                    import redis
                    self.redis = redis.Redis()

                def _generate_sid(self):
                    return str(uuid.uuid4())

                def _get_signer(self, app):
                    if not app.secret_key:
                        return None
                    return Signer(app.secret_key, salt='flask-session',
                                  key_derivation='hmac')

                def open_session(self, app, request):
                    """
                    程序刚启动时执行，需要返回一个session对象
                    """
                    sid = request.cookies.get(app.session_cookie_name)
                    if not sid:
                        sid = self._generate_sid()
                        return self.session_class(sid=sid)

                    signer = self._get_signer(app)
                    try:
                        sid_as_bytes = signer.unsign(sid)
                        sid = sid_as_bytes.decode()
                    except BadSignature:
                        sid = self._generate_sid()
                        return self.session_class(sid=sid)

                    # session保存在redis中
                    # val = self.redis.get(sid)
                    # session保存在内存中
                    val = self.container.get(sid)

                    if val is not None:
                        try:
                            data = json.loads(val)
                            return self.session_class(data, sid=sid)
                        except:
                            return self.session_class(sid=sid)
                    return self.session_class(sid=sid)

                def save_session(self, app, session, response):
                    """
                    程序结束前执行，可以保存session中所有的值
                    如：
                        保存到resit
                        写入到用户cookie
                    """
                    domain = self.get_cookie_domain(app)
                    path = self.get_cookie_path(app)
                    httponly = self.get_cookie_httponly(app)
                    secure = self.get_cookie_secure(app)
                    expires = self.get_expiration_time(app, session)

                    val = json.dumps(dict(session))

                    # session保存在redis中
                    # self.redis.setex(name=session.sid, value=val, time=app.permanent_session_lifetime)
                    # session保存在内存中
                    self.container.setdefault(session.sid, val)

                    session_id = self._get_signer(app).sign(want_bytes(session.sid))

                    response.set_cookie(app.session_cookie_name, session_id,
                                        expires=expires, httponly=httponly,
                                        domain=domain, path=path, secure=secure)


第三方session

::

 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 """
 pip3 install redis
 pip3 install flask-session

 """


 from flask import Flask, session, redirect
 from flask.ext.session import Session


 app = Flask(__name__)
 app.debug = True
 app.secret_key = 'asdfasdfasd'


 app.config['SESSION_TYPE'] = 'redis'
 from redis import Redis
 app.config['SESSION_REDIS'] = Redis(host='192.168.0.94',port='6379')
 Session(app)


 @app.route('/login')
 def login():
    session['username'] = 'alex'
    return redirect('/index')


 @app.route('/index')
 def index():
    name = session['username']
    return name


 if __name__ == '__main__':
    app.run()


Django和Flask中session的区别
-------------------------------------------

::

 '''
 Django中，session保存在服务端的数据库中，数据库中保存请求用户的所有数据，服务端数据中{'随机字符串'：加密后的客户相关信息}
 请求完成后，把随机字符串作为值，返回给客户端，保存在客户端的cookie中，键为：sessionid，值为：服务端返回的随机字符串；即{'sessionid':'随机字符串'}
        
 Flask中，服务端什么都不存，用户第一次请求时，在内存中生成一个空字典，将这个空字典加密后，返回给客户端，保存在客户端的cookie中，键为’session',值为:加密后的字典
 下次访问时，读取客户端cookie中key为session对应的值
 然后进行解密（如果不能按之前的的加密方式对应个解密方式解密，即认为第一次请求，重新生成空字典），解密成功后，可以对字典进行操作，保存新数据在字典中，请求完成后，会重新加密这个字典,返回个客户端保存

 '''