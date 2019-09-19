import uuid

from flask import Blueprint, request, jsonify

from app.tasks.email import send_email

bp_account = Blueprint('account', __name__)


@bp_account.route('/password/forgot/', methods=['POST'])
def reset_password():
    email = request.form['email']
    token = str(uuid.uuid4())
    content = u'请点击链接重置密码：http://example.com/password/reset/?token=%s' % token
    send_email.delay(email, content)
    return jsonify(code=0, message=u'发送成功')
