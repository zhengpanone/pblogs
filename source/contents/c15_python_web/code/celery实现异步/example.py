import uuid

from flask import Flask, request, jsonify
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(include=['example'],
                broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def send_email(to, subject, content):
    return do_send_email(to, subject, content)


@app.route('/password/forgot/', methods=['POST'])
def reset_password():
    email = request.form['email']
    token = str(uuid.uuid4())
    content = u'请点击链接重置密码：http://example.com/password/reset/?token=%s' % token
    send_email.delay(email, content)
    return jsonify(code=0, message=u'发送成功')


if __name__ == '__main__':
    app.run()
