from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class TelephoneConvert(BaseConverter):
    regex = r'1[85734]\d{9}'

app.url_map.converters['tel'] = TelephoneConvert

@app.route('/telephone/<tel:my_tel>')
def telconvert(my_tel):
    return 'tel:%s'%my_tel


if __name__ == '__main__':
    app.run(debug=True)