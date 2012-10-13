import os
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/physics/planck_constant', endpoint='planck_constant')
def hello():
    dict = {'value': 6.62606957E-34, 'units': 'joule*seconds', 'citation': 'http://en.wikipedia.org/wiki/Planck_constant','name': 'planck constant'};
    data = json.dumps(dict)
    return data

@app.route('/physics/standard_gravity', endpoint='standard_gravity')
def hello():
    dict = {'value': 9.80665, 'units': 'meters/(seconds^2)', 'citation': 'http://en.wikipedia.org/wiki/Standard_gravity','name': 'standard gravity'};
    data = json.dumps(dict)
    return data

@app.route('/physics/electron_mass', endpoint='electron_mass')
def hello():
    dict = {'value': .510998910, 'units': 'mega electron*volts/c^2', 'citation': 'http://en.wikipedia.org/wiki/Electron_rest_mass','name': 'Electron rest mass'};
    data = json.dumps(dict)
    return data

@app.route('/physics/proton_mass', endpoint='electron_mass')
def hello():
    dict = {'value': 938.272046, 'units': 'mega electron*volts/c^2', 'citation': 'http://en.wikipedia.org/wiki/Proton','name': 'Proton rest mass'};
    data = json.dumps(dict)
    return data

@app.route('/physics/neutron_mass', endpoint='electron_mass')
def hello():
    dict = {'value': 939.565378, 'units': 'mega electron*volts/c^2', 'citation': 'http://en.wikipedia.org/wiki/Neutron','name': 'Neutron rest mass'};
    data = json.dumps(dict)
    return data

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)