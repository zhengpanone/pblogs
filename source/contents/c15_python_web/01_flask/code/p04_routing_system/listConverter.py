from flask import Flask
from werkzeug.routing import BaseConverter
app = Flask(__name__)


class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')
    
app.url_map.converters['list'] = ListConverter

@app.route('/posts/<list:boards>')    
def list_route(boards):
    return 'converter %s' %boards


if __name__ == '__main__':
    app.run(debug=True)