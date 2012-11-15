import os
from flask import Flask, render_template, json


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('../welcomepage/templates/page_not_found.html'), 404

@app.route('/')
def index():
    return  render_template('Constants.html')

@app.route('/physics/planck_constant', endpoint='planck_constant')
def index():
    json_file = open('templates/json/planck_constant.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('planck_constant.html',data=data)

@app.route('/physics/characteristic_impedance_of_vacuum', endpoint='characteristic_impedance_of_vacuum')
def index():
    json_file = open('templates/json/characteristic_impedance_of_a_vacuum.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('characteristic_impedance_of_vacuum.html',data=data)

@app.route('/physics/vacuum_permittivity', endpoint='vacuum_permittivity')
def index():
    json_file = open('templates/json/vacuum_permittivity.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('vacuum_permittivity.html',data=data)

@app.route('/physics/standard_gravity', endpoint='standard_gravity')
def index():
    json_file = open('templates/json/standard_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('standard_gravity.html',data=data)

@app.route('/physics/electron_mass', endpoint='electron_mass')
def index():
    json_file = open('templates/json/electron_mass.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('electron_mass.html',data=data)

@app.route('/physics/proton_mass', endpoint='proton_mass')
def index():
    json_file = open('templates/json/proton_mass.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('proton_mass.html',data=data)

@app.route('/physics/neutron_mass', endpoint='neutron_mass')
def index():
    json_file = open('templates/json/neutron_mass.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('neutron_mass.html',data=data)

@app.route('/physics/elementary_charge', endpoint='elementary_charge')
def index():
    json_file = open('templates/json/elementary_charge.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('elementary_charge.html',data=data)

@app.route('/physics/planck_constant_json', endpoint='planck_constant_json')
def index():
    return render_template('json/planck_constant.json')

@app.route('/physics/characteristic_impedance_of_vacuum_json', endpoint='characteristic_impedance_of_vacuum_json')
def index():
    return render_template('json/characteristic_impedance_of_a_vacuum.json')

@app.route('/physics/vacuum_permittivity_json', endpoint='vacuum_permittivity_json')
def index():
    return render_template('json/vacuum_permittivity.json')

@app.route('/physics/standard_gravity_json', endpoint='standard_gravity_json')
def index():
    return render_template('json/standard_gravity.json')

@app.route('/physics/electron_mass_json', endpoint='electron_mass_json')
def index():
    return render_template('json/electron_mass.json')

@app.route('/physics/proton_mass_json', endpoint='proton_mass_json')
def index():
    return render_template('json/proton_mass.json')

@app.route('/physics/neutron_mass_json', endpoint='neutron_mass_json')
def index():
    return render_template('json/neutron_mass.json')

@app.route('/physics/elementary_charge_json', endpoint='elementary_charge_json')
def index():
    return render_template('json/elementary_charge.json')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)