import os
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def index():
    return  render_template('Constants.html')

@app.route('/physics/planck_constant', endpoint='planck_constant')
def index():
    return  render_template('planck_constant.json')

@app.route('/physics/planck_constant_json', endpoint='planck_constant_json')
def index():
    dict = {'value': 6.62606957e-34, 'units': 'joule*seconds', 'citation': 'http://physics.nist.gov/cgi-bin/cuu/Value?z0|search_for=universal_in!','name': 'planck constant'};
    data = json.dumps(dict)
    return data

@app.route('/physics/characteristic_impedance_of_vacuum', endpoint='characteristic_impedance_of_vacuum')
def index():
    dict = {'value': 376.730313461, 'units': 'ohms', 'citation': 'http://physics.nist.gov/cgi-bin/cuu/Value?z0|search_for=universal_in!','name': 'Characteristic impedance of a vacuum'};
    data = json.dumps(dict)
    return data

@app.route('/physics/vacuum_permittivity', endpoint='vacuum_permittivity')
def index():
    dict = {'value': 8.854187817E-12, 'units': 'farad/meters', 'citation': 'http://physics.nist.gov/cgi-bin/cuu/Value?ep0|search_for=universal_in!','name': 'vacuum permittivity'};
    data = json.dumps(dict)
    return data

@app.route('/physics/standard_gravity', endpoint='standard_gravity')
def index():
    dict = {'value': 9.80665, 'units': 'meters/(seconds^2)', 'citation': 'http://en.wikipedia.org/wiki/Standard_gravity','name': 'standard gravity'};
    data = json.dumps(dict)
    return data

@app.route('/physics/electron_mass', endpoint='electron_mass')
def index():
    dict = {'value': .510998910, 'units': 'mega electron*volts/c^2', 'citation': 'http://en.wikipedia.org/wiki/Electron_rest_mass','name': 'Electron rest mass'};
    data = json.dumps(dict)
    return data

@app.route('/physics/proton_mass', endpoint='proton_mass')
def index():
    dict = {'value': 938.272046, 'units': 'mega electron*volts/c^2', 'citation': 'http://en.wikipedia.org/wiki/Proton','name': 'Proton rest mass'};
    data = json.dumps(dict)
    return data

@app.route('/physics/neutron_mass', endpoint='neutron_mass')
def index():
    dict = {'value': 939.565378, 'units': 'mega electron*volts/c^2', 'citation': 'http://en.wikipedia.org/wiki/Neutron','name': 'Neutron rest mass'};
    data = json.dumps(dict)
    return data

@app.route('/physics/elementary_charge', endpoint='elementary_charge')
def index():
    dict = {'value': 1.602176565E-19, 'units': 'Coulomb', 'citation': 'http://en.wikipedia.org/wiki/Elementary_charge','name': 'Elementary charge'};
    data = json.dumps(dict)
    return data

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)