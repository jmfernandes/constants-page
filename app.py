import os
import json
from flask import Flask

app = Flask('plancksconstant')
app = Flask(__name__.split('.')[0])

@app.route('/physics/planck')
def hello():
    dict = {'value': 6.62606957E-34, 'units': 'joule*seconds', 'citation': 'http://en.wikipedia.org/wiki/Planck_constant','name': 'Planck's constant'};
    data = json.dumps(dict)
    return data

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)