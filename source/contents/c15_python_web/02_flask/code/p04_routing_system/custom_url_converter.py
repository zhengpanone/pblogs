from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class TelephoneConveter(BaseConverter):
    regx = r'1[85734]\d{9}'


app.url_map.converters['tel'] = TelephoneConveter


@app.route("/")
def index():
    return "Hello Flask!"


@app.route("/user/<string:user_name>")
def user_info(user_name: str):
    return f"Your name {user_name}"


@app.route("/telephone/<tel:tel_num>")
def my_tel(tel_num):
    return f"You phone {tel_num}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
