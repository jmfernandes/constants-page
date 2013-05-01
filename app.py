import os
from flask import Flask, render_template, json


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def index():
    return  render_template('Constants.html')

@app.route('/physics/planck_constant', endpoint='planck_constant')
def index():
    json_file = open('templates/json/physics/planck_constant.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/physics/characteristic_impedance_of_vacuum', endpoint='characteristic_impedance_of_vacuum')
def index():
    json_file = open('templates/json/physics/characteristic_impedance_of_a_vacuum.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/physics/vacuum_permittivity', endpoint='vacuum_permittivity')
def index():
    json_file = open('templates/json/physics/vacuum_permittivity.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/physics/standard_gravity', endpoint='standard_gravity')
def index():
    json_file = open('templates/json/physics/standard_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/physics/electron_mass', endpoint='electron_mass')
def index():
    json_file = open('templates/json/physics/electron_mass.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/physics/proton_mass', endpoint='proton_mass')
def index():
    json_file = open('templates/json/physics/proton_mass.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/physics/neutron_mass', endpoint='neutron_mass')
def index():
    json_file = open('templates/json/physics/neutron_mass.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/physics/elementary_charge', endpoint='elementary_charge')
def index():
    json_file = open('templates/json/physics/elementary_charge.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/physics/speed_of_light', endpoint='speed_of_light')
def index():
    json_file = open('templates/json/physics/speed_of_light.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/physics/vacuum_permeability', endpoint='vacuum_permeability')
def index():
    json_file = open('templates/json/physics/vacuum_permeability.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""Chemistry Web Pages"""

@app.route('/chemistry/atomic_mass_unit', endpoint='atomic_mass_unit')
def index():
    json_file = open('templates/json/chemistry/atomic_mass_unit.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/avogadros_number', endpoint='avogadros_number')
def index():
    json_file = open('templates/json/chemistry/avogadros_number.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/bohr_radius', endpoint='bohr_radius')
def index():
    json_file = open('templates/json/chemistry/bohr_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/molar_gas_constant', endpoint='molar_gas_constant')
def index():
    json_file = open('templates/json/chemistry/molar_gas_constant.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""Biology Web Pages"""

@app.route('/biology/blood_volume_of_human', endpoint='blood_volume_of_human')
def index():
    json_file = open('templates/json/biology/blood_volume_of_human.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""Natural Web Pages"""

@app.route('/natural/equatorial_radius_of_earth', endpoint='equatorial_radius_of_earth')
def index():
    json_file = open('templates/json/natural/equatorial_radius_of_earth.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)


"""JSON FILE PAGES"""

@app.route('/physics/planck_constant_json', endpoint='planck_constant_json')
def index():
    return render_template('json/physics/planck_constant.json')

@app.route('/physics/characteristic_impedance_of_vacuum_json', endpoint='characteristic_impedance_of_vacuum_json')
def index():
    return render_template('json/physics/characteristic_impedance_of_a_vacuum.json')

@app.route('/physics/vacuum_permittivity_json', endpoint='vacuum_permittivity_json')
def index():
    return render_template('json/physics/vacuum_permittivity.json')

@app.route('/physics/standard_gravity_json', endpoint='standard_gravity_json')
def index():
    return render_template('json/physics/standard_gravity.json')

@app.route('/physics/electron_mass_json', endpoint='electron_mass_json')
def index():
    return render_template('json/physics/electron_mass.json')

@app.route('/physics/proton_mass_json', endpoint='proton_mass_json')
def index():
    return render_template('json/physics/proton_mass.json')

@app.route('/physics/neutron_mass_json', endpoint='neutron_mass_json')
def index():
    return render_template('json/physics/neutron_mass.json')

@app.route('/physics/elementary_charge_json', endpoint='elementary_charge_json')
def index():
    return render_template('json/physics/elementary_charge.json')

@app.route('/physics/speed_of_light_json', endpoint='elementary_charge_json')
def index():
    return render_template('json/physics/speed_of_light.json')

@app.route('/physics/vacuum_permeability_json', endpoint='vacuum_permeability_json')
def index():
    return render_template('json/physics/vacuum_permeability.json')

"""Chemistry Constants"""

@app.route('/chemistry/atomic_mass_unit_json', endpoint='/chemistry/atomic_mass_unit_json')
def index():
    return render_template('json/chemistry/atomic_mass_unit.json')

@app.route('/chemistry/avogadros_number_json', endpoint='/chemistry/avogadros_number_json')
def index():
    return render_template('json/chemistry/avogadros_number.json')

@app.route('/chemistry/bohr_radius_json', endpoint='/chemistry/bohr_radius_json')
def index():
    return render_template('json/chemistry/bohr_radius.json')

@app.route('/chemistry/molar_gas_constant_json', endpoint='/chemistry/molar_gas_constant_json')
def index():
    return render_template('json/chemistry/molar_gas_constant.json')

"""Biology Constants"""

@app.route('/biology/blood_volume_of_human_json', endpoint='/biology/blood_volume_of_human_json')
def index():
    return render_template('json/biology/blood_volume_of_human.json')

"""Natural Constants"""

@app.route('/natural/equatorial_radius_of_earth_json', endpoint='/natural/equatorial_radius_of_earth_json')
def index():
    return render_template('json/natural/equatorial_radius_of_earth.json')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)