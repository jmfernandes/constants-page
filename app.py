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

@app.route('/physics/speed_of_sound', endpoint='speed_of_sound')
def index():
    json_file = open('templates/json/physics/speed_of_sound.json')
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

"""density"""

@app.route('/chemistry/density/aluminum', endpoint='density/aluminum')
def index():
    json_file = open('templates/json/chemistry/density/aluminum.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/asphalt', endpoint='density/asphalt')
def index():
    json_file = open('templates/json/chemistry/density/asphalt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/beeswax', endpoint='density/beeswax')
def index():
    json_file = open('templates/json/chemistry/density/beeswax.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/bituminous_coal', endpoint='density/bituminous_coal')
def index():
    json_file = open('templates/json/chemistry/density/bituminous_coal.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/bone', endpoint='density/bone')
def index():
    json_file = open('templates/json/chemistry/density/bone.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/brass', endpoint='density/brass')
def index():
    json_file = open('templates/json/chemistry/density/brass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/brick', endpoint='density/brick')
def index():
    json_file = open('templates/json/chemistry/density/brick.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/cement', endpoint='density/cement')
def index():
    json_file = open('templates/json/chemistry/density/cement.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/chalk', endpoint='density/chalk')
def index():
    json_file = open('templates/json/chemistry/density/chalk.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/charcoal', endpoint='density/charcoal')
def index():
    json_file = open('templates/json/chemistry/density/charcoal.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/copper', endpoint='density/copper')
def index():
    json_file = open('templates/json/chemistry/density/copper.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/cork', endpoint='density/cork')
def index():
    json_file = open('templates/json/chemistry/density/cork.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/cotton', endpoint='density/cotton')
def index():
    json_file = open('templates/json/chemistry/density/cotton.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/diamond', endpoint='density/diamond')
def index():
    json_file = open('templates/json/chemistry/density/diamond.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/earth', endpoint='density/earth')
def index():
    json_file = open('templates/json/chemistry/density/earth.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/glass', endpoint='density/glass')
def index():
    json_file = open('templates/json/chemistry/density/glass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/gold', endpoint='density/gold')
def index():
    json_file = open('templates/json/chemistry/density/gold.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/ice', endpoint='density/ice')
def index():
    json_file = open('templates/json/chemistry/density/ice.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/iron', endpoint='density/iron')
def index():
    json_file = open('templates/json/chemistry/density/iron.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/lead', endpoint='density/lead')
def index():
    json_file = open('templates/json/chemistry/density/lead.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/leather', endpoint='density/leather')
def index():
    json_file = open('templates/json/chemistry/density/leather.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/mercury', endpoint='density/mercury')
def index():
    json_file = open('templates/json/chemistry/density/mercury.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/nickel', endpoint='density/nickel')
def index():
    json_file = open('templates/json/chemistry/density/nickel.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/oak_wood', endpoint='density/oak_wood')
def index():
    json_file = open('templates/json/chemistry/density/oak_wood.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/paper', endpoint='density/paper')
def index():
    json_file = open('templates/json/chemistry/density/paper.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/plaster', endpoint='density/plaster')
def index():
    json_file = open('templates/json/chemistry/density/plaster.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/rubber', endpoint='density/rubber')
def index():
    json_file = open('templates/json/chemistry/density/rubber.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/salt', endpoint='density/salt')
def index():
    json_file = open('templates/json/chemistry/density/salt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/sand', endpoint='density/sand')
def index():
    json_file = open('templates/json/chemistry/density/sand.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/silicon', endpoint='density/silicon')
def index():
    json_file = open('templates/json/chemistry/density/silicon.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/steel', endpoint='density/steel')
def index():
    json_file = open('templates/json/chemistry/density/steel.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/stone', endpoint='density/stone')
def index():
    json_file = open('templates/json/chemistry/density/stone.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/tin', endpoint='density/tin')
def index():
    json_file = open('templates/json/chemistry/density/tin.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/tungsten', endpoint='density/tungsten')
def index():
    json_file = open('templates/json/chemistry/density/tungsten.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/density/uranium', endpoint='density/uranium')
def index():
    json_file = open('templates/json/chemistry/density/uranium.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""melting point"""

@app.route('/chemistry/melting_point/aluminum', endpoint='melting_point/aluminum')
def index():
    json_file = open('templates/json/chemistry/melting_point/aluminum.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/asphalt', endpoint='melting_point/asphalt')
def index():
    json_file = open('templates/json/chemistry/melting_point/asphalt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/beeswax', endpoint='melting_point/beeswax')
def index():
    json_file = open('templates/json/chemistry/melting_point/beeswax.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/bituminous_coal', endpoint='melting_point/bituminous_coal')
def index():
    json_file = open('templates/json/chemistry/melting_point/bituminous_coal.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/bone', endpoint='melting_point/bone')
def index():
    json_file = open('templates/json/chemistry/melting_point/bone.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/brass', endpoint='melting_point/brass')
def index():
    json_file = open('templates/json/chemistry/melting_point/brass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/brick', endpoint='melting_point/brick')
def index():
    json_file = open('templates/json/chemistry/melting_point/brick.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/cement', endpoint='melting_point/cement')
def index():
    json_file = open('templates/json/chemistry/melting_point/cement.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/chalk', endpoint='melting_point/chalk')
def index():
    json_file = open('templates/json/chemistry/melting_point/chalk.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/charcoal', endpoint='melting_point/charcoal')
def index():
    json_file = open('templates/json/chemistry/melting_point/charcoal.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/copper', endpoint='melting_point/copper')
def index():
    json_file = open('templates/json/chemistry/melting_point/copper.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/cork', endpoint='melting_point/cork')
def index():
    json_file = open('templates/json/chemistry/melting_point/cork.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/cotton', endpoint='melting_point/cotton')
def index():
    json_file = open('templates/json/chemistry/melting_point/cotton.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/diamond', endpoint='melting_point/diamond')
def index():
    json_file = open('templates/json/chemistry/melting_point/diamond.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/earth', endpoint='melting_point/earth')
def index():
    json_file = open('templates/json/chemistry/melting_point/earth.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/glass', endpoint='melting_point/glass')
def index():
    json_file = open('templates/json/chemistry/melting_point/glass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/gold', endpoint='melting_point/gold')
def index():
    json_file = open('templates/json/chemistry/melting_point/gold.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/ice', endpoint='melting_point/ice')
def index():
    json_file = open('templates/json/chemistry/melting_point/ice.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/iron', endpoint='melting_point/iron')
def index():
    json_file = open('templates/json/chemistry/melting_point/iron.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/lead', endpoint='melting_point/lead')
def index():
    json_file = open('templates/json/chemistry/melting_point/lead.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/leather', endpoint='melting_point/leather')
def index():
    json_file = open('templates/json/chemistry/melting_point/leather.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/mercury', endpoint='melting_point/mercury')
def index():
    json_file = open('templates/json/chemistry/melting_point/mercury.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/nickel', endpoint='melting_point/nickel')
def index():
    json_file = open('templates/json/chemistry/melting_point/nickel.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/oak_wood', endpoint='melting_point/oak_wood')
def index():
    json_file = open('templates/json/chemistry/melting_point/oak_wood.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/paper', endpoint='melting_point/paper')
def index():
    json_file = open('templates/json/chemistry/melting_point/paper.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/plaster', endpoint='melting_point/plaster')
def index():
    json_file = open('templates/json/chemistry/melting_point/plaster.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/rubber', endpoint='melting_point/rubber')
def index():
    json_file = open('templates/json/chemistry/melting_point/rubber.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/salt', endpoint='melting_point/salt')
def index():
    json_file = open('templates/json/chemistry/melting_point/salt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/sand', endpoint='melting_point/sand')
def index():
    json_file = open('templates/json/chemistry/melting_point/sand.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/silicon', endpoint='melting_point/silicon')
def index():
    json_file = open('templates/json/chemistry/melting_point/silicon.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/steel', endpoint='melting_point/steel')
def index():
    json_file = open('templates/json/chemistry/melting_point/steel.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/stone', endpoint='melting_point/stone')
def index():
    json_file = open('templates/json/chemistry/melting_point/stone.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/tin', endpoint='melting_point/tin')
def index():
    json_file = open('templates/json/chemistry/melting_point/tin.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/tungsten', endpoint='melting_point/tungsten')
def index():
    json_file = open('templates/json/chemistry/melting_point/tungsten.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/melting_point/uranium', endpoint='melting_point/uranium')
def index():
    json_file = open('templates/json/chemistry/melting_point/uranium.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""specific heat"""

@app.route('/chemistry/specific_heat/aluminum', endpoint='specific_heat/aluminum')
def index():
    json_file = open('templates/json/chemistry/specific_heat/aluminum.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/asphalt', endpoint='specific_heat/asphalt')
def index():
    json_file = open('templates/json/chemistry/specific_heat/asphalt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/beeswax', endpoint='specific_heat/beeswax')
def index():
    json_file = open('templates/json/chemistry/specific_heat/beeswax.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/bituminous_coal', endpoint='specific_heat/bituminous_coal')
def index():
    json_file = open('templates/json/chemistry/specific_heat/bituminous_coal.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/bone', endpoint='specific_heat/bone')
def index():
    json_file = open('templates/json/chemistry/specific_heat/bone.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/brass', endpoint='specific_heat/brass')
def index():
    json_file = open('templates/json/chemistry/specific_heat/brass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/brick', endpoint='specific_heat/brick')
def index():
    json_file = open('templates/json/chemistry/specific_heat/brick.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/cement', endpoint='specific_heat/cement')
def index():
    json_file = open('templates/json/chemistry/specific_heat/cement.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/chalk', endpoint='specific_heat/chalk')
def index():
    json_file = open('templates/json/chemistry/specific_heat/chalk.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/charcoal', endpoint='specific_heat/charcoal')
def index():
    json_file = open('templates/json/chemistry/specific_heat/charcoal.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/copper', endpoint='specific_heat/copper')
def index():
    json_file = open('templates/json/chemistry/specific_heat/copper.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/cork', endpoint='specific_heat/cork')
def index():
    json_file = open('templates/json/chemistry/specific_heat/cork.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/cotton', endpoint='specific_heat/cotton')
def index():
    json_file = open('templates/json/chemistry/specific_heat/cotton.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/diamond', endpoint='specific_heat/diamond')
def index():
    json_file = open('templates/json/chemistry/specific_heat/diamond.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/earth', endpoint='specific_heat/earth')
def index():
    json_file = open('templates/json/chemistry/specific_heat/earth.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/glass', endpoint='specific_heat/glass')
def index():
    json_file = open('templates/json/chemistry/specific_heat/glass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/gold', endpoint='specific_heat/gold')
def index():
    json_file = open('templates/json/chemistry/specific_heat/gold.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/ice', endpoint='specific_heat/ice')
def index():
    json_file = open('templates/json/chemistry/specific_heat/ice.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/iron', endpoint='specific_heat/iron')
def index():
    json_file = open('templates/json/chemistry/specific_heat/Iron.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/lead', endpoint='specific_heat/lead')
def index():
    json_file = open('templates/json/chemistry/specific_heat/lead.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/leather', endpoint='specific_heat/leather')
def index():
    json_file = open('templates/json/chemistry/specific_heat/leather.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/mercury', endpoint='specific_heat/mercury')
def index():
    json_file = open('templates/json/chemistry/specific_heat/mercury.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/nickel', endpoint='specific_heat/nickel')
def index():
    json_file = open('templates/json/chemistry/specific_heat/nickel.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/oak_wood', endpoint='specific_heat/oak_wood')
def index():
    json_file = open('templates/json/chemistry/specific_heat/oak_wood.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/paper', endpoint='specific_heat/paper')
def index():
    json_file = open('templates/json/chemistry/specific_heat/paper.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/plaster', endpoint='specific_heat/plaster')
def index():
    json_file = open('templates/json/chemistry/specific_heat/plaster.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/rubber', endpoint='specific_heat/rubber')
def index():
    json_file = open('templates/json/chemistry/specific_heat/rubber.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/salt', endpoint='specific_heat/salt')
def index():
    json_file = open('templates/json/chemistry/specific_heat/salt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/sand', endpoint='specific_heat/sand')
def index():
    json_file = open('templates/json/chemistry/specific_heat/sand.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/silicon', endpoint='specific_heat/silicon')
def index():
    json_file = open('templates/json/chemistry/specific_heat/silicon.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/steel', endpoint='specific_heat/steel')
def index():
    json_file = open('templates/json/chemistry/specific_heat/steel.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/stone', endpoint='specific_heat/stone')
def index():
    json_file = open('templates/json/chemistry/specific_heat/stone.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/tin', endpoint='specific_heat/tin')
def index():
    json_file = open('templates/json/chemistry/specific_heat/tin.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/tungsten', endpoint='specific_heat/tungsten')
def index():
    json_file = open('templates/json/chemistry/specific_heat/tungsten.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/chemistry/specific_heat/uranium', endpoint='specific_heat/uranium')
def index():
    json_file = open('templates/json/chemistry/specific_heat/uranium.json')
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

@app.route('/biology/life_expectancy', endpoint='life_expectancy')
def index():
    json_file = open('templates/json/biology/life_expectancy.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/theobromine_cocoa', endpoint='theobromine_cocoa')
def index():
    json_file = open('templates/json/biology/theobromine_cocoa.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""human LD50"""

@app.route('/biology/human_ld50_vitamin_a', endpoint='human_ld50_vitamin_a')
def index():
    json_file = open('templates/json/biology/human_ld50_vitamin_a.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_thc', endpoint='human_ld50_thc')
def index():
    json_file = open('templates/json/biology/human_ld50_thc.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_thc_inhalation', endpoint='human_ld50_thc_inhalation')
def index():
    json_file = open('templates/json/biology/human_ld50_thc_inhalation.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_psilocypbin', endpoint='human_ld50_psilocypbin')
def index():
    json_file = open('templates/json/biology/human_ld50_psilocypbin.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_nicotine', endpoint='human_ld50_nicotine')
def index():
    json_file = open('templates/json/biology/human_ld50_nicotine.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_nicotine_iv', endpoint='human_ld50_nicotine_iv')
def index():
    json_file = open('templates/json/biology/human_ld50_nicotine_iv.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_nerve_gas', endpoint='human_ld50_nerve_gas')
def index():
    json_file = open('templates/json/biology/human_ld50_nerve_gas.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_lsd', endpoint='human_ld50_lsd')
def index():
    json_file = open('templates/json/biology/human_ld50_lsd.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_caffeine', endpoint='human_ld50_caffeine')
def index():
    json_file = open('templates/json/biology/human_ld50_caffeine.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_aspirin', endpoint='human_ld50_aspirin')
def index():
    json_file = open('templates/json/biology/human_ld50_aspirin.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_acetaminophen', endpoint='human_ld50_acetaminophen')
def index():
    json_file = open('templates/json/biology/human_ld50_acetaminophen.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

@app.route('/biology/human_ld50_theobromine', endpoint='human_ld50_theobromine')
def index():
    json_file = open('templates/json/biology/human_ld50_theobromine.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""dog LD50"""

@app.route('/biology/dog_ld50_theobromine', endpoint='dog_ld50_theobromine')
def index():
    json_file = open('templates/json/biology/dogld50_theobromine.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)


"""Cat LD50"""

@app.route('/biology/cat_ld50_theobromine', endpoint='cat_ld50_theobromine')
def index():
    json_file = open('templates/json/biology/catld50_theobromine.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)



"""Natural Web Pages"""


"""earth"""
@app.route('/natural/earth/axial_tilt', endpoint='/earth/axial_tilt')
def index():
    json_file = open('templates/json/natural/earth/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/black_body_temperature', endpoint='/earth/black_body_temperature')
def index():
    json_file = open('templates/json/natural/earth/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/distance_from_sun', endpoint='/earth/distance_from_sun')
def index():
    json_file = open('templates/json/natural/earth/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/equatorial_radius', endpoint='/earth/equatorial_radius')
def index():
    json_file = open('templates/json/natural/earth/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/escape_velocity', endpoint='/earth/escape_velocity')
def index():
    json_file = open('templates/json/natural/earth/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/length_of_day', endpoint='/earth/length_of_day')
def index():
    json_file = open('templates/json/natural/earth/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/mass', endpoint='/earth/mass')
def index():
    json_file = open('templates/json/natural/earth/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/mean_density', endpoint='/earth/mean_density')
def index():
    json_file = open('templates/json/natural/earth/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/mean_orbital_velocity', endpoint='/earth/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/earth/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/orbital_period', endpoint='/earth/orbital_period')
def index():
    json_file = open('templates/json/natural/earth/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/polar_radius', endpoint='/earth/polar_radius')
def index():
    json_file = open('templates/json/natural/earth/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/solar_irradiance', endpoint='/earth/solar_irradiance')
def index():
    json_file = open('templates/json/natural/earth/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/surface_gravity', endpoint='/earth/surface_gravity')
def index():
    json_file = open('templates/json/natural/earth/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/earth/volume', endpoint='/earth/volume')
def index():
    json_file = open('templates/json/natural/earth/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""jupiter"""
@app.route('/natural/jupiter/axial_tilt', endpoint='/jupiter/axial_tilt')
def index():
    json_file = open('templates/json/natural/jupiter/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/black_body_temperature', endpoint='/jupiter/black_body_temperature')
def index():
    json_file = open('templates/json/natural/jupiter/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/distance_from_sun', endpoint='/jupiter/distance_from_sun')
def index():
    json_file = open('templates/json/natural/jupiter/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/equatorial_radius', endpoint='/jupiter/equatorial_radius')
def index():
    json_file = open('templates/json/natural/jupiter/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/escape_velocity', endpoint='/jupiter/escape_velocity')
def index():
    json_file = open('templates/json/natural/jupiter/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/length_of_day', endpoint='/jupiter/length_of_day')
def index():
    json_file = open('templates/json/natural/jupiter/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/mass', endpoint='/jupiter/mass')
def index():
    json_file = open('templates/json/natural/jupiter/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/mean_density', endpoint='/jupiter/mean_density')
def index():
    json_file = open('templates/json/natural/jupiter/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/mean_orbital_velocity', endpoint='/jupiter/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/jupiter/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/orbital_period', endpoint='/jupiter/orbital_period')
def index():
    json_file = open('templates/json/natural/jupiter/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/polar_radius', endpoint='/jupiter/polar_radius')
def index():
    json_file = open('templates/json/natural/jupiter/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/solar_irradiance', endpoint='/jupiter/solar_irradiance')
def index():
    json_file = open('templates/json/natural/jupiter/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/surface_gravity', endpoint='/jupiter/surface_gravity')
def index():
    json_file = open('templates/json/natural/jupiter/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/jupiter/volume', endpoint='/jupiter/volume')
def index():
    json_file = open('templates/json/natural/jupiter/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""mars"""
@app.route('/natural/mars/axial_tilt', endpoint='/mars/axial_tilt')
def index():
    json_file = open('templates/json/natural/mars/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/black_body_temperature', endpoint='/mars/black_body_temperature')
def index():
    json_file = open('templates/json/natural/mars/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/distance_from_sun', endpoint='/mars/distance_from_sun')
def index():
    json_file = open('templates/json/natural/mars/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/equatorial_radius', endpoint='/mars/equatorial_radius')
def index():
    json_file = open('templates/json/natural/mars/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/escape_velocity', endpoint='/mars/escape_velocity')
def index():
    json_file = open('templates/json/natural/mars/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/length_of_day', endpoint='/mars/length_of_day')
def index():
    json_file = open('templates/json/natural/mars/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/mass', endpoint='/mars/mass')
def index():
    json_file = open('templates/json/natural/mars/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/mean_density', endpoint='/mars/mean_density')
def index():
    json_file = open('templates/json/natural/mars/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/mean_orbital_velocity', endpoint='/mars/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/mars/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/orbital_period', endpoint='/mars/orbital_period')
def index():
    json_file = open('templates/json/natural/mars/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/polar_radius', endpoint='/mars/polar_radius')
def index():
    json_file = open('templates/json/natural/mars/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/solar_irradiance', endpoint='/mars/solar_irradiance')
def index():
    json_file = open('templates/json/natural/mars/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/surface_gravity', endpoint='/mars/surface_gravity')
def index():
    json_file = open('templates/json/natural/mars/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mars/volume', endpoint='/mars/volume')
def index():
    json_file = open('templates/json/natural/mars/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""mercury"""
@app.route('/natural/mercury/axial_tilt', endpoint='/mercury/axial_tilt')
def index():
    json_file = open('templates/json/natural/mercury/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/black_body_temperature', endpoint='/mercury/black_body_temperature')
def index():
    json_file = open('templates/json/natural/mercury/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/distance_from_sun', endpoint='/mercury/distance_from_sun')
def index():
    json_file = open('templates/json/natural/mercury/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/equatorial_radius', endpoint='/mercury/equatorial_radius')
def index():
    json_file = open('templates/json/natural/mercury/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/escape_velocity', endpoint='/mercury/escape_velocity')
def index():
    json_file = open('templates/json/natural/mercury/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/length_of_day', endpoint='/mercury/length_of_day')
def index():
    json_file = open('templates/json/natural/mercury/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/mass', endpoint='/mercury/mass')
def index():
    json_file = open('templates/json/natural/mercury/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/mean_density', endpoint='/mercury/mean_density')
def index():
    json_file = open('templates/json/natural/mercury/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/mean_orbital_velocity', endpoint='/mercury/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/mercury/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/orbital_period', endpoint='/mercury/orbital_period')
def index():
    json_file = open('templates/json/natural/mercury/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/polar_radius', endpoint='/mercury/polar_radius')
def index():
    json_file = open('templates/json/natural/mercury/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/solar_irradiance', endpoint='/mercury/solar_irradiance')
def index():
    json_file = open('templates/json/natural/mercury/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/surface_gravity', endpoint='/mercury/surface_gravity')
def index():
    json_file = open('templates/json/natural/mercury/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/mercury/volume', endpoint='/mercury/volume')
def index():
    json_file = open('templates/json/natural/mercury/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""moon"""
@app.route('/natural/moon/axial_tilt', endpoint='/moon/axial_tilt')
def index():
    json_file = open('templates/json/natural/moon/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/black_body_temperature', endpoint='/moon/black_body_temperature')
def index():
    json_file = open('templates/json/natural/moon/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/distance_from_sun', endpoint='/moon/distance_from_sun')
def index():
    json_file = open('templates/json/natural/moon/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/equatorial_radius', endpoint='/moon/equatorial_radius')
def index():
    json_file = open('templates/json/natural/moon/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/escape_velocity', endpoint='/moon/escape_velocity')
def index():
    json_file = open('templates/json/natural/moon/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/length_of_day', endpoint='/moon/length_of_day')
def index():
    json_file = open('templates/json/natural/moon/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/mass', endpoint='/moon/mass')
def index():
    json_file = open('templates/json/natural/moon/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/mean_density', endpoint='/moon/mean_density')
def index():
    json_file = open('templates/json/natural/moon/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/mean_orbital_velocity', endpoint='/moon/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/moon/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/orbital_period', endpoint='/moon/orbital_period')
def index():
    json_file = open('templates/json/natural/moon/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/polar_radius', endpoint='/moon/polar_radius')
def index():
    json_file = open('templates/json/natural/moon/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/solar_irradiance', endpoint='/moon/solar_irradiance')
def index():
    json_file = open('templates/json/natural/moon/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/surface_gravity', endpoint='/moon/surface_gravity')
def index():
    json_file = open('templates/json/natural/moon/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/moon/volume', endpoint='/moon/volume')
def index():
    json_file = open('templates/json/natural/moon/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""neptune"""
@app.route('/natural/neptune/axial_tilt', endpoint='/neptune/axial_tilt')
def index():
    json_file = open('templates/json/natural/neptune/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/black_body_temperature', endpoint='/neptune/black_body_temperature')
def index():
    json_file = open('templates/json/natural/neptune/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/distance_from_sun', endpoint='/neptune/distance_from_sun')
def index():
    json_file = open('templates/json/natural/neptune/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/equatorial_radius', endpoint='/neptune/equatorial_radius')
def index():
    json_file = open('templates/json/natural/neptune/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/escape_velocity', endpoint='/neptune/escape_velocity')
def index():
    json_file = open('templates/json/natural/neptune/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/length_of_day', endpoint='/neptune/length_of_day')
def index():
    json_file = open('templates/json/natural/neptune/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/mass', endpoint='/neptune/mass')
def index():
    json_file = open('templates/json/natural/neptune/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/mean_density', endpoint='/neptune/mean_density')
def index():
    json_file = open('templates/json/natural/neptune/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/mean_orbital_velocity', endpoint='/neptune/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/neptune/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/orbital_period', endpoint='/neptune/orbital_period')
def index():
    json_file = open('templates/json/natural/neptune/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/polar_radius', endpoint='/neptune/polar_radius')
def index():
    json_file = open('templates/json/natural/neptune/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/solar_irradiance', endpoint='/neptune/solar_irradiance')
def index():
    json_file = open('templates/json/natural/neptune/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/surface_gravity', endpoint='/neptune/surface_gravity')
def index():
    json_file = open('templates/json/natural/neptune/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/neptune/volume', endpoint='/neptune/volume')
def index():
    json_file = open('templates/json/natural/neptune/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""saturn"""
@app.route('/natural/saturn/axial_tilt', endpoint='/saturn/axial_tilt')
def index():
    json_file = open('templates/json/natural/saturn/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/black_body_temperature', endpoint='/saturn/black_body_temperature')
def index():
    json_file = open('templates/json/natural/saturn/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/distance_from_sun', endpoint='/saturn/distance_from_sun')
def index():
    json_file = open('templates/json/natural/saturn/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/equatorial_radius', endpoint='/saturn/equatorial_radius')
def index():
    json_file = open('templates/json/natural/saturn/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/escape_velocity', endpoint='/saturn/escape_velocity')
def index():
    json_file = open('templates/json/natural/saturn/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/length_of_day', endpoint='/saturn/length_of_day')
def index():
    json_file = open('templates/json/natural/saturn/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/mass', endpoint='/saturn/mass')
def index():
    json_file = open('templates/json/natural/saturn/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/mean_density', endpoint='/saturn/mean_density')
def index():
    json_file = open('templates/json/natural/saturn/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/mean_orbital_velocity', endpoint='/saturn/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/saturn/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/orbital_period', endpoint='/saturn/orbital_period')
def index():
    json_file = open('templates/json/natural/saturn/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/polar_radius', endpoint='/saturn/polar_radius')
def index():
    json_file = open('templates/json/natural/saturn/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/solar_irradiance', endpoint='/saturn/solar_irradiance')
def index():
    json_file = open('templates/json/natural/saturn/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/surface_gravity', endpoint='/saturn/surface_gravity')
def index():
    json_file = open('templates/json/natural/saturn/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/saturn/volume', endpoint='/saturn/volume')
def index():
    json_file = open('templates/json/natural/saturn/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""uranus"""
@app.route('/natural/uranus/axial_tilt', endpoint='/uranus/axial_tilt')
def index():
    json_file = open('templates/json/natural/uranus/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/black_body_temperature', endpoint='/uranus/black_body_temperature')
def index():
    json_file = open('templates/json/natural/uranus/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/distance_from_sun', endpoint='/uranus/distance_from_sun')
def index():
    json_file = open('templates/json/natural/uranus/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/equatorial_radius', endpoint='/uranus/equatorial_radius')
def index():
    json_file = open('templates/json/natural/uranus/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/escape_velocity', endpoint='/uranus/escape_velocity')
def index():
    json_file = open('templates/json/natural/uranus/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/length_of_day', endpoint='/uranus/length_of_day')
def index():
    json_file = open('templates/json/natural/uranus/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/mass', endpoint='/uranus/mass')
def index():
    json_file = open('templates/json/natural/uranus/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/mean_density', endpoint='/uranus/mean_density')
def index():
    json_file = open('templates/json/natural/uranus/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/mean_orbital_velocity', endpoint='/uranus/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/uranus/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/orbital_period', endpoint='/uranus/orbital_period')
def index():
    json_file = open('templates/json/natural/uranus/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/polar_radius', endpoint='/uranus/polar_radius')
def index():
    json_file = open('templates/json/natural/uranus/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/solar_irradiance', endpoint='/uranus/solar_irradiance')
def index():
    json_file = open('templates/json/natural/uranus/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/surface_gravity', endpoint='/uranus/surface_gravity')
def index():
    json_file = open('templates/json/natural/uranus/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/uranus/volume', endpoint='/uranus/volume')
def index():
    json_file = open('templates/json/natural/uranus/volume.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)

"""Venus"""
@app.route('/natural/venus/axial_tilt', endpoint='/venus/axial_tilt')
def index():
    json_file = open('templates/json/natural/venus/axial_tilt.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/black_body_temperature', endpoint='/venus/black_body_temperature')
def index():
    json_file = open('templates/json/natural/venus/black_body_temperature.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/distance_from_sun', endpoint='/venus/distance_from_sun')
def index():
    json_file = open('templates/json/natural/venus/distance_from_sun.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/equatorial_radius', endpoint='/venus/equatorial_radius')
def index():
    json_file = open('templates/json/natural/venus/equatorial_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/escape_velocity', endpoint='/venus/escape_velocity')
def index():
    json_file = open('templates/json/natural/venus/escape_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/length_of_day', endpoint='/venus/length_of_day')
def index():
    json_file = open('templates/json/natural/venus/length_of_day.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/mass', endpoint='/venus/mass')
def index():
    json_file = open('templates/json/natural/venus/mass.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/mean_density', endpoint='/venus/mean_density')
def index():
    json_file = open('templates/json/natural/venus/mean_density.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/mean_orbital_velocity', endpoint='/venus/mean_orbital_velocity')
def index():
    json_file = open('templates/json/natural/venus/mean_orbital_velocity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/orbital_period', endpoint='/venus/orbital_period')
def index():
    json_file = open('templates/json/natural/venus/orbital_period.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/polar_radius', endpoint='/venus/polar_radius')
def index():
    json_file = open('templates/json/natural/venus/polar_radius.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/solar_irradiance', endpoint='/venus/solar_irradiance')
def index():
    json_file = open('templates/json/natural/venus/solar_irradiance.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/surface_gravity', endpoint='/venus/surface_gravity')
def index():
    json_file = open('templates/json/natural/venus/surface_gravity.json')
    data = json.load(json_file)
    json_file.close()
    return  render_template('webpage.html',data=data)
@app.route('/natural/venus/volume', endpoint='/venus/volume')
def index():
    json_file = open('templates/json/natural/venus/volume.json')
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

@app.route('/physics/speed_of_light_json', endpoint='speed_of_light_json')
def index():
    return render_template('json/physics/speed_of_light.json')

@app.route('/physics/speed_of_sound_json', endpoint='speed_of_sound_json')
def index():
    return render_template('json/physics/speed_of_sound.json')

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

"""density"""
@app.route('/chemistry/density/aluminum_json', endpoint='/density/aluminum_json')
def index():
    return render_template('json/chemistry/density/aluminum.json')

@app.route('/chemistry/density/asphalt_json', endpoint='/density/asphalt_json')
def index():
    return render_template('json/chemistry/density/asphalt.json')

@app.route('/chemistry/density/beeswax_json', endpoint='/density/beeswax_json')
def index():
    return render_template('json/chemistry/density/beeswax.json')

@app.route('/chemistry/density/bituminous_coal_json', endpoint='/density/bituminous_coal_json')
def index():
    return render_template('json/chemistry/density/bituminous_coal.json')

@app.route('/chemistry/density/bone_json', endpoint='/density/bone_json')
def index():
    return render_template('json/chemistry/density/bone.json')

@app.route('/chemistry/density/brass_json', endpoint='/density/brass_json')
def index():
    return render_template('json/chemistry/density/brass.json')

@app.route('/chemistry/density/brick_json', endpoint='/density/brick_json')
def index():
    return render_template('json/chemistry/density/brick.json')

@app.route('/chemistry/density/cement_json', endpoint='/density/cement_json')
def index():
    return render_template('json/chemistry/density/cement.json')

@app.route('/chemistry/density/chalk_json', endpoint='/density/chalk_json')
def index():
    return render_template('json/chemistry/density/chalk.json')

@app.route('/chemistry/density/charcoal_json', endpoint='/density/charcoal_json')
def index():
    return render_template('json/chemistry/density/charcoal.json')

@app.route('/chemistry/density/copper_json', endpoint='/density/copper_json')
def index():
    return render_template('json/chemistry/density/copper.json')

@app.route('/chemistry/density/cork_json', endpoint='/density/cork_json')
def index():
    return render_template('json/chemistry/density/cork.json')

@app.route('/chemistry/density/cotton_json', endpoint='/density/cotton_json')
def index():
    return render_template('json/chemistry/density/cotton.json')

@app.route('/chemistry/density/diamond_json', endpoint='/density/diamond_json')
def index():
    return render_template('json/chemistry/density/diamond.json')

@app.route('/chemistry/density/earth_json', endpoint='/density/earth_json')
def index():
    return render_template('json/chemistry/density/earth.json')

@app.route('/chemistry/density/glass_json', endpoint='/density/glass_json')
def index():
    return render_template('json/chemistry/density/glass.json')

@app.route('/chemistry/density/gold_json', endpoint='/density/gold_json')
def index():
    return render_template('json/chemistry/density/gold.json')

@app.route('/chemistry/density/ice_json', endpoint='/density/ice_json')
def index():
    return render_template('json/chemistry/density/ice.json')

@app.route('/chemistry/density/iron_json', endpoint='/density/iron_json')
def index():
    return render_template('json/chemistry/density/iron.json')

@app.route('/chemistry/density/lead_json', endpoint='/density/lead_json')
def index():
    return render_template('json/chemistry/density/lead.json')

@app.route('/chemistry/density/leather_json', endpoint='/density/leather_json')
def index():
    return render_template('json/chemistry/density/leather.json')

@app.route('/chemistry/density/mercury_json', endpoint='/density/mercury_json')
def index():
    return render_template('json/chemistry/density/mercury.json')

@app.route('/chemistry/density/nickel_json', endpoint='/density/nickel_json')
def index():
    return render_template('json/chemistry/density/nickel.json')

@app.route('/chemistry/density/oak_wood_json', endpoint='/density/oak_wood_json')
def index():
    return render_template('json/chemistry/density/oak_wood.json')

@app.route('/chemistry/density/paper_json', endpoint='/density/paper_json')
def index():
    return render_template('json/chemistry/density/paper.json')

@app.route('/chemistry/density/plaster_json', endpoint='/density/plaster_json')
def index():
    return render_template('json/chemistry/density/plaster.json')

@app.route('/chemistry/density/rubber_json', endpoint='/density/rubber_json')
def index():
    return render_template('json/chemistry/density/rubber.json')

@app.route('/chemistry/density/salt_json', endpoint='/density/salt_json')
def index():
    return render_template('json/chemistry/density/salt.json')

@app.route('/chemistry/density/sand_json', endpoint='/density/sand_json')
def index():
    return render_template('json/chemistry/density/sand.json')

@app.route('/chemistry/density/silicon_json', endpoint='/density/silicon_json')
def index():
    return render_template('json/chemistry/density/silicon.json')

@app.route('/chemistry/density/steel_json', endpoint='/density/steel_json')
def index():
    return render_template('json/chemistry/density/steel.json')

@app.route('/chemistry/density/stone_json', endpoint='/density/stone_json')
def index():
    return render_template('json/chemistry/density/stone.json')

@app.route('/chemistry/density/tin_json', endpoint='/density/tin_json')
def index():
    return render_template('json/chemistry/density/tin.json')

@app.route('/chemistry/density/tungsten_json', endpoint='/density/tungsten_json')
def index():
    return render_template('json/chemistry/density/tungsten.json')

@app.route('/chemistry/density/uranium_json', endpoint='/density/uranium_json')
def index():
    return render_template('json/chemistry/density/uranium.json')


"""melting point"""
@app.route('/chemistry/melting_point/aluminum_json', endpoint='/melting_point/aluminum_json')
def index():
    return render_template('json/chemistry/melting_point/aluminum.json')

@app.route('/chemistry/melting_point/asphalt_json', endpoint='/melting_point/asphalt_json')
def index():
    return render_template('json/chemistry/melting_point/asphalt.json')

@app.route('/chemistry/melting_point/beeswax_json', endpoint='/melting_point/beeswax_json')
def index():
    return render_template('json/chemistry/melting_point/beeswax.json')

@app.route('/chemistry/melting_point/bituminous_coal_json', endpoint='/melting_point/bituminous_coal_json')
def index():
    return render_template('json/chemistry/melting_point/bituminous_coal.json')

@app.route('/chemistry/melting_point/bone_json', endpoint='/melting_point/bone_json')
def index():
    return render_template('json/chemistry/melting_point/bone.json')

@app.route('/chemistry/melting_point/brass_json', endpoint='/melting_point/brass_json')
def index():
    return render_template('json/chemistry/melting_point/brass.json')

@app.route('/chemistry/melting_point/brick_json', endpoint='/melting_point/brick_json')
def index():
    return render_template('json/chemistry/melting_point/brick.json')

@app.route('/chemistry/melting_point/cement_json', endpoint='/melting_point/cement_json')
def index():
    return render_template('json/chemistry/melting_point/cement.json')

@app.route('/chemistry/melting_point/chalk_json', endpoint='/melting_point/chalk_json')
def index():
    return render_template('json/chemistry/melting_point/chalk.json')

@app.route('/chemistry/melting_point/charcoal_json', endpoint='/melting_point/charcoal_json')
def index():
    return render_template('json/chemistry/melting_point/charcoal.json')

@app.route('/chemistry/melting_point/copper_json', endpoint='/melting_point/copper_json')
def index():
    return render_template('json/chemistry/melting_point/copper.json')

@app.route('/chemistry/melting_point/cork_json', endpoint='/melting_point/cork_json')
def index():
    return render_template('json/chemistry/melting_point/cork.json')

@app.route('/chemistry/melting_point/cotton_json', endpoint='/melting_point/cotton_json')
def index():
    return render_template('json/chemistry/melting_point/cotton.json')

@app.route('/chemistry/melting_point/diamond_json', endpoint='/melting_point/diamond_json')
def index():
    return render_template('json/chemistry/melting_point/diamond.json')

@app.route('/chemistry/melting_point/earth_json', endpoint='/melting_point/earth_json')
def index():
    return render_template('json/chemistry/melting_point/earth.json')

@app.route('/chemistry/melting_point/glass_json', endpoint='/melting_point/glass_json')
def index():
    return render_template('json/chemistry/melting_point/glass.json')

@app.route('/chemistry/melting_point/gold_json', endpoint='/melting_point/gold_json')
def index():
    return render_template('json/chemistry/melting_point/gold.json')

@app.route('/chemistry/melting_point/ice_json', endpoint='/melting_point/ice_json')
def index():
    return render_template('json/chemistry/melting_point/ice.json')

@app.route('/chemistry/melting_point/iron_json', endpoint='/melting_point/iron_json')
def index():
    return render_template('json/chemistry/melting_point/iron.json')

@app.route('/chemistry/melting_point/lead_json', endpoint='/melting_point/lead_json')
def index():
    return render_template('json/chemistry/melting_point/lead.json')

@app.route('/chemistry/melting_point/leather_json', endpoint='/melting_point/leather_json')
def index():
    return render_template('json/chemistry/melting_point/leather.json')

@app.route('/chemistry/melting_point/mercury_json', endpoint='/melting_point/mercury_json')
def index():
    return render_template('json/chemistry/melting_point/mercury.json')

@app.route('/chemistry/melting_point/nickel_json', endpoint='/melting_point/nickel_json')
def index():
    return render_template('json/chemistry/melting_point/nickel.json')

@app.route('/chemistry/melting_point/oak_wood_json', endpoint='/melting_point/oak_wood_json')
def index():
    return render_template('json/chemistry/melting_point/oak_wood.json')

@app.route('/chemistry/melting_point/paper_json', endpoint='/melting_point/paper_json')
def index():
    return render_template('json/chemistry/melting_point/paper.json')

@app.route('/chemistry/melting_point/plaster_json', endpoint='/melting_point/plaster_json')
def index():
    return render_template('json/chemistry/melting_point/plaster.json')

@app.route('/chemistry/melting_point/rubber_json', endpoint='/melting_point/rubber_json')
def index():
    return render_template('json/chemistry/melting_point/rubber.json')

@app.route('/chemistry/melting_point/salt_json', endpoint='/melting_point/salt_json')
def index():
    return render_template('json/chemistry/melting_point/salt.json')

@app.route('/chemistry/melting_point/sand_json', endpoint='/melting_point/sand_json')
def index():
    return render_template('json/chemistry/melting_point/sand.json')

@app.route('/chemistry/melting_point/silicon_json', endpoint='/melting_point/silicon_json')
def index():
    return render_template('json/chemistry/melting_point/silicon.json')

@app.route('/chemistry/melting_point/steel_json', endpoint='/melting_point/steel_json')
def index():
    return render_template('json/chemistry/melting_point/steel.json')

@app.route('/chemistry/melting_point/stone_json', endpoint='/melting_point/stone_json')
def index():
    return render_template('json/chemistry/melting_point/stone.json')

@app.route('/chemistry/melting_point/tin_json', endpoint='/melting_point/tin_json')
def index():
    return render_template('json/chemistry/melting_point/tin.json')

@app.route('/chemistry/melting_point/tungsten_json', endpoint='/melting_point/tungsten_json')
def index():
    return render_template('json/chemistry/melting_point/tungsten.json')

@app.route('/chemistry/melting_point/uranium_json', endpoint='/melting_point/uranium_json')
def index():
    return render_template('json/chemistry/melting_point/uranium.json')

"""specific heat"""
@app.route('/chemistry/specific_heat/aluminum_json', endpoint='/specific_heat/aluminum_json')
def index():
    return render_template('json/chemistry/specific_heat/aluminum.json')

@app.route('/chemistry/specific_heat/asphalt_json', endpoint='/specific_heat/asphalt_json')
def index():
    return render_template('json/chemistry/specific_heat/asphalt.json')

@app.route('/chemistry/specific_heat/beeswax_json', endpoint='/specific_heat/beeswax_json')
def index():
    return render_template('json/chemistry/specific_heat/beeswax.json')

@app.route('/chemistry/specific_heat/bituminous_coal_json', endpoint='/specific_heat/bituminous_coal_json')
def index():
    return render_template('json/chemistry/specific_heat/bituminous_coal.json')

@app.route('/chemistry/specific_heat/bone_json', endpoint='/specific_heat/bone_json')
def index():
    return render_template('json/chemistry/specific_heat/bone.json')

@app.route('/chemistry/specific_heat/brass_json', endpoint='/specific_heat/brass_json')
def index():
    return render_template('json/chemistry/specific_heat/brass.json')

@app.route('/chemistry/specific_heat/brick_json', endpoint='/specific_heat/brick_json')
def index():
    return render_template('json/chemistry/specific_heat/brick.json')

@app.route('/chemistry/specific_heat/cement_json', endpoint='/specific_heat/cement_json')
def index():
    return render_template('json/chemistry/specific_heat/cement.json')

@app.route('/chemistry/specific_heat/chalk_json', endpoint='/specific_heat/chalk_json')
def index():
    return render_template('json/chemistry/specific_heat/chalk.json')

@app.route('/chemistry/specific_heat/charcoal_json', endpoint='/specific_heat/charcoal_json')
def index():
    return render_template('json/chemistry/specific_heat/charcoal.json')

@app.route('/chemistry/specific_heat/copper_json', endpoint='/specific_heat/copper_json')
def index():
    return render_template('json/chemistry/specific_heat/copper.json')

@app.route('/chemistry/specific_heat/cork_json', endpoint='/specific_heat/cork_json')
def index():
    return render_template('json/chemistry/specific_heat/cork.json')

@app.route('/chemistry/specific_heat/cotton_json', endpoint='/specific_heat/cotton_json')
def index():
    return render_template('json/chemistry/specific_heat/cotton.json')

@app.route('/chemistry/specific_heat/diamond_json', endpoint='/specific_heat/diamond_json')
def index():
    return render_template('json/chemistry/specific_heat/diamond.json')

@app.route('/chemistry/specific_heat/earth_json', endpoint='/specific_heat/earth_json')
def index():
    return render_template('json/chemistry/specific_heat/earth.json')

@app.route('/chemistry/specific_heat/glass_json', endpoint='/specific_heat/glass_json')
def index():
    return render_template('json/chemistry/specific_heat/glass.json')

@app.route('/chemistry/specific_heat/gold_json', endpoint='/specific_heat/gold_json')
def index():
    return render_template('json/chemistry/specific_heat/gold.json')

@app.route('/chemistry/specific_heat/ice_json', endpoint='/specific_heat/ice_json')
def index():
    return render_template('json/chemistry/specific_heat/ice.json')

@app.route('/chemistry/specific_heat/iron_json', endpoint='/specific_heat/iron_json')
def index():
    return render_template('json/chemistry/specific_heat/iron.json')

@app.route('/chemistry/specific_heat/lead_json', endpoint='/specific_heat/lead_json')
def index():
    return render_template('json/chemistry/specific_heat/lead.json')

@app.route('/chemistry/specific_heat/leather_json', endpoint='/specific_heat/leather_json')
def index():
    return render_template('json/chemistry/specific_heat/leather.json')

@app.route('/chemistry/specific_heat/mercury_json', endpoint='/specific_heat/mercury_json')
def index():
    return render_template('json/chemistry/specific_heat/mercury.json')

@app.route('/chemistry/specific_heat/nickel_json', endpoint='/specific_heat/nickel_json')
def index():
    return render_template('json/chemistry/specific_heat/nickel.json')

@app.route('/chemistry/specific_heat/oak_wood_json', endpoint='/specific_heat/oak_wood_json')
def index():
    return render_template('json/chemistry/specific_heat/oak_wood.json')

@app.route('/chemistry/specific_heat/paper_json', endpoint='/specific_heat/paper_json')
def index():
    return render_template('json/chemistry/specific_heat/paper.json')

@app.route('/chemistry/specific_heat/plaster_json', endpoint='/specific_heat/plaster_json')
def index():
    return render_template('json/chemistry/specific_heat/plaster.json')

@app.route('/chemistry/specific_heat/rubber_json', endpoint='/specific_heat/rubber_json')
def index():
    return render_template('json/chemistry/specific_heat/rubber.json')

@app.route('/chemistry/specific_heat/salt_json', endpoint='/specific_heat/salt_json')
def index():
    return render_template('json/chemistry/specific_heat/salt.json')

@app.route('/chemistry/specific_heat/sand_json', endpoint='/specific_heat/sand_json')
def index():
    return render_template('json/chemistry/specific_heat/sand.json')

@app.route('/chemistry/specific_heat/silicon_json', endpoint='/specific_heat/silicon_json')
def index():
    return render_template('json/chemistry/specific_heat/silicon.json')

@app.route('/chemistry/specific_heat/steel_json', endpoint='/specific_heat/steel_json')
def index():
    return render_template('json/chemistry/specific_heat/steel.json')

@app.route('/chemistry/specific_heat/stone_json', endpoint='/specific_heat/stone_json')
def index():
    return render_template('json/chemistry/specific_heat/stone.json')

@app.route('/chemistry/specific_heat/tin_json', endpoint='/specific_heat/tin_json')
def index():
    return render_template('json/chemistry/specific_heat/tin.json')

@app.route('/chemistry/specific_heat/tungsten_json', endpoint='/specific_heat/tungsten_json')
def index():
    return render_template('json/chemistry/specific_heat/tungsten.json')

@app.route('/chemistry/specific_heat/uranium_json', endpoint='/specific_heat/uranium_json')
def index():
    return render_template('json/chemistry/specific_heat/uranium.json')




"""Biology Constants"""

@app.route('/biology/blood_volume_of_human_json', endpoint='/biology/blood_volume_of_human_json')
def index():
    return render_template('json/biology/blood_volume_of_human.json')

@app.route('/biology/life_expectancy_json', endpoint='/biology/life_expectancy_json')
def index():
    return render_template('json/biology/life_expectancy.json')

@app.route('/biology/human_ld50_vitamin_a_json', endpoint='/biology/human_ld50_vitamin_a_json')
def index():
    return render_template('json/biology/human_ld50_vitamin_a.json')

@app.route('/biology/human_ld50_thc_json', endpoint='/biology/human_ld50_thc_json')
def index():
    return render_template('json/biology/human_ld50_thc.json')

@app.route('/biology/human_ld50_thc_inhalation_json', endpoint='/biology/human_ld50_thc_inhalation_json')
def index():
    return render_template('json/biology/human_ld50_thc_inhalation.json')

@app.route('/biology/human_ld50_psilocypbin_json', endpoint='/biology/human_ld50_psilocypbin_json')
def index():
    return render_template('json/biology/human_ld50_psilocypbin.json')

@app.route('/biology/human_ld50_nicotine_json', endpoint='/biology/human_ld50_nicotine_json')
def index():
    return render_template('json/biology/human_ld50_nicotine.json')

@app.route('/biology/human_ld50_nicotine_iv_json', endpoint='/biology/human_ld50_nicotine_iv_json')
def index():
    return render_template('json/biology/human_ld50_nicotine_iv.json')

@app.route('/biology/human_ld50_nerve_gas_json', endpoint='/biology/human_ld50_nerve_gas_json')
def index():
    return render_template('json/biology/human_ld50_nerve_gas.json')

@app.route('/biology/human_ld50_lsd_json', endpoint='/biology/human_ld50_lsd_json')
def index():
    return render_template('json/biology/human_ld50_lsd.json')

@app.route('/biology/human_ld50_caffeine_json', endpoint='/biology/human_ld50_caffeine_json')
def index():
    return render_template('json/biology/human_ld50_caffeine.json')

@app.route('/biology/human_ld50_aspirin_json', endpoint='/biology/human_ld50_aspirin_json')
def index():
    return render_template('json/biology/human_ld50_aspirin.json')

@app.route('/biology/human_ld50_acetaminophen_json', endpoint='/biology/human_ld50_acetaminophen_json')
def index():
    return render_template('json/biology/human_ld50_acetaminophen.json')

@app.route('/biology/human_ld50_theobromine_json', endpoint='/biology/human_ld50_theobromine_json')
def index():
    return render_template('json/biology/human_ld50_theobromine.json')

@app.route('/biology/theobromine_cocoa_json', endpoint='/biology/theobromine_cocoa_json')
def index():
    return render_template('json/biology/theobromine_cocoa.json')

"""dog ld50"""

@app.route('/biology/dog_ld50_theobromine_json', endpoint='/biology/dog_ld50_theobromine_json')
def index():
    return render_template('json/biology/dogld50_theobromine.json')


"""cat LD50"""

@app.route('/biology/cat_ld50_theobromine_json', endpoint='/biology/cat_ld50_theobromine_json')
def index():
    return render_template('json/biology/catld50_theobromine.json')


"""Natural Constants"""

"""Earth"""
@app.route('/natural/earth/axial_tilt_json', endpoint='/natural/earth/axial_tilt_json')
def index():
    return render_template('json/natural/earth/axial_tilt.json')
@app.route('/natural/earth/black_body_temperature_json', endpoint='/natural/earth/black_body_temperature_json')
def index():
    return render_template('json/natural/earth/black_body_temperature.json')
@app.route('/natural/earth/distance_from_sun_json', endpoint='/natural/earth/distance_from_sun_json')
def index():
    return render_template('json/natural/earth/distance_from_sun.json')
@app.route('/natural/earth/equatorial_radius_json', endpoint='/natural/earth/equatorial_radius_json')
def index():
    return render_template('json/natural/earth/equatorial_radius.json')
@app.route('/natural/earth/escape_velocity_json', endpoint='/natural/earth/escape_velocity_json')
def index():
    return render_template('json/natural/earth/escape_velocity.json')
@app.route('/natural/earth/length_of_day_json', endpoint='/natural/earth/length_of_day_json')
def index():
    return render_template('json/natural/earth/length_of_day.json')
@app.route('/natural/earth/mass_json', endpoint='/natural/earth/mass_json')
def index():
    return render_template('json/natural/earth/mass.json')
@app.route('/natural/earth/mean_density_json', endpoint='/natural/earth/mean_density_json')
def index():
    return render_template('json/natural/earth/mean_density.json')
@app.route('/natural/earth/mean_orbital_velocity_json', endpoint='/natural/earth/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/earth/mean_orbital_velocity.json')
@app.route('/natural/earth/orbital_period_json', endpoint='/natural/earth/orbital_period_json')
def index():
    return render_template('json/natural/earth/orbital_period.json')
@app.route('/natural/earth/polar_radius_json', endpoint='/natural/earth/polar_radius_json')
def index():
    return render_template('json/natural/earth/polar_radius.json')
@app.route('/natural/earth/solar_irradiance_json', endpoint='/natural/earth/solar_irradiance_json')
def index():
    return render_template('json/natural/earth/solar_irradiance.json')
@app.route('/natural/earth/surface_gravity_json', endpoint='/natural/earth/surface_gravity_json')
def index():
    return render_template('json/natural/earth/surface_gravity.json')
@app.route('/natural/earth/volume_json', endpoint='/natural/earth/volume_json')
def index():
    return render_template('json/natural/earth/volume.json')


"""Jupiter"""
@app.route('/natural/jupiter/axial_tilt_json', endpoint='/natural/jupiter/axial_tilt_json')
def index():
    return render_template('json/natural/jupiter/axial_tilt.json')
@app.route('/natural/jupiter/black_body_temperature_json', endpoint='/natural/jupiter/black_body_temperature_json')
def index():
    return render_template('json/natural/jupiter/black_body_temperature.json')
@app.route('/natural/jupiter/distance_from_sun_json', endpoint='/natural/jupiter/distance_from_sun_json')
def index():
    return render_template('json/natural/jupiter/distance_from_sun.json')
@app.route('/natural/jupiter/equatorial_radius_json', endpoint='/natural/jupiter/equatorial_radius_json')
def index():
    return render_template('json/natural/jupiter/equatorial_radius.json')
@app.route('/natural/jupiter/escape_velocity_json', endpoint='/natural/jupiter/escape_velocity_json')
def index():
    return render_template('json/natural/jupiter/escape_velocity.json')
@app.route('/natural/jupiter/length_of_day_json', endpoint='/natural/jupiter/length_of_day_json')
def index():
    return render_template('json/natural/jupiter/length_of_day.json')
@app.route('/natural/jupiter/mass_json', endpoint='/natural/jupiter/mass_json')
def index():
    return render_template('json/natural/jupiter/mass.json')
@app.route('/natural/jupiter/mean_density_json', endpoint='/natural/jupiter/mean_density_json')
def index():
    return render_template('json/natural/jupiter/mean_density.json')
@app.route('/natural/jupiter/mean_orbital_velocity_json', endpoint='/natural/jupiter/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/jupiter/mean_orbital_velocity.json')
@app.route('/natural/jupiter/orbital_period_json', endpoint='/natural/jupiter/orbital_period_json')
def index():
    return render_template('json/natural/jupiter/orbital_period.json')
@app.route('/natural/jupiter/polar_radius_json', endpoint='/natural/jupiter/polar_radius_json')
def index():
    return render_template('json/natural/jupiter/polar_radius.json')
@app.route('/natural/jupiter/solar_irradiance_json', endpoint='/natural/jupiter/solar_irradiance_json')
def index():
    return render_template('json/natural/jupiter/solar_irradiance.json')
@app.route('/natural/jupiter/surface_gravity_json', endpoint='/natural/jupiter/surface_gravity_json')
def index():
    return render_template('json/natural/jupiter/surface_gravity.json')
@app.route('/natural/jupiter/volume_json', endpoint='/natural/jupiter/volume_json')
def index():
    return render_template('json/natural/jupiter/volume.json')


"""Mars"""
@app.route('/natural/mars/axial_tilt_json', endpoint='/natural/mars/axial_tilt_json')
def index():
    return render_template('json/natural/mars/axial_tilt.json')
@app.route('/natural/mars/black_body_temperature_json', endpoint='/natural/mars/black_body_temperature_json')
def index():
    return render_template('json/natural/mars/black_body_temperature.json')
@app.route('/natural/mars/distance_from_sun_json', endpoint='/natural/mars/distance_from_sun_json')
def index():
    return render_template('json/natural/mars/distance_from_sun.json')
@app.route('/natural/mars/equatorial_radius_json', endpoint='/natural/mars/equatorial_radius_json')
def index():
    return render_template('json/natural/mars/equatorial_radius.json')
@app.route('/natural/mars/escape_velocity_json', endpoint='/natural/mars/escape_velocity_json')
def index():
    return render_template('json/natural/mars/escape_velocity.json')
@app.route('/natural/mars/length_of_day_json', endpoint='/natural/mars/length_of_day_json')
def index():
    return render_template('json/natural/mars/length_of_day.json')
@app.route('/natural/mars/mass_json', endpoint='/natural/mars/mass_json')
def index():
    return render_template('json/natural/mars/mass.json')
@app.route('/natural/mars/mean_density_json', endpoint='/natural/mars/mean_density_json')
def index():
    return render_template('json/natural/mars/mean_density.json')
@app.route('/natural/mars/mean_orbital_velocity_json', endpoint='/natural/mars/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/mars/mean_orbital_velocity.json')
@app.route('/natural/mars/orbital_period_json', endpoint='/natural/mars/orbital_period_json')
def index():
    return render_template('json/natural/mars/orbital_period.json')
@app.route('/natural/mars/polar_radius_json', endpoint='/natural/mars/polar_radius_json')
def index():
    return render_template('json/natural/mars/polar_radius.json')
@app.route('/natural/mars/solar_irradiance_json', endpoint='/natural/mars/solar_irradiance_json')
def index():
    return render_template('json/natural/mars/solar_irradiance.json')
@app.route('/natural/mars/surface_gravity_json', endpoint='/natural/mars/surface_gravity_json')
def index():
    return render_template('json/natural/mars/surface_gravity.json')
@app.route('/natural/mars/volume_json', endpoint='/natural/mars/volume_json')
def index():
    return render_template('json/natural/mars/volume.json')


"""Mercury"""
@app.route('/natural/mercury/axial_tilt_json', endpoint='/natural/mercury/axial_tilt_json')
def index():
    return render_template('json/natural/mercury/axial_tilt.json')
@app.route('/natural/mercury/black_body_temperature_json', endpoint='/natural/mercury/black_body_temperature_json')
def index():
    return render_template('json/natural/mercury/black_body_temperature.json')
@app.route('/natural/mercury/distance_from_sun_json', endpoint='/natural/mercury/distance_from_sun_json')
def index():
    return render_template('json/natural/mercury/distance_from_sun.json')
@app.route('/natural/mercury/equatorial_radius_json', endpoint='/natural/mercury/equatorial_radius_json')
def index():
    return render_template('json/natural/mercury/equatorial_radius.json')
@app.route('/natural/mercury/escape_velocity_json', endpoint='/natural/mercury/escape_velocity_json')
def index():
    return render_template('json/natural/mercury/escape_velocity.json')
@app.route('/natural/mercury/length_of_day_json', endpoint='/natural/mercury/length_of_day_json')
def index():
    return render_template('json/natural/mercury/length_of_day.json')
@app.route('/natural/mercury/mass_json', endpoint='/natural/mercury/mass_json')
def index():
    return render_template('json/natural/mercury/mass.json')
@app.route('/natural/mercury/mean_density_json', endpoint='/natural/mercury/mean_density_json')
def index():
    return render_template('json/natural/mercury/mean_density.json')
@app.route('/natural/mercury/mean_orbital_velocity_json', endpoint='/natural/mercury/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/mercury/mean_orbital_velocity.json')
@app.route('/natural/mercury/orbital_period_json', endpoint='/natural/mercury/orbital_period_json')
def index():
    return render_template('json/natural/mercury/orbital_period.json')
@app.route('/natural/mercury/polar_radius_json', endpoint='/natural/mercury/polar_radius_json')
def index():
    return render_template('json/natural/mercury/polar_radius.json')
@app.route('/natural/mercury/solar_irradiance_json', endpoint='/natural/mercury/solar_irradiance_json')
def index():
    return render_template('json/natural/mercury/solar_irradiance.json')
@app.route('/natural/mercury/surface_gravity_json', endpoint='/natural/mercury/surface_gravity_json')
def index():
    return render_template('json/natural/mercury/surface_gravity.json')
@app.route('/natural/mercury/volume_json', endpoint='/natural/mercury/volume_json')
def index():
    return render_template('json/natural/mercury/volume.json')


"""Moon"""
@app.route('/natural/moon/axial_tilt_json', endpoint='/natural/moon/axial_tilt_json')
def index():
    return render_template('json/natural/moon/axial_tilt.json')
@app.route('/natural/moon/black_body_temperature_json', endpoint='/natural/moon/black_body_temperature_json')
def index():
    return render_template('json/natural/moon/black_body_temperature.json')
@app.route('/natural/moon/distance_from_sun_json', endpoint='/natural/moon/distance_from_sun_json')
def index():
    return render_template('json/natural/moon/distance_from_sun.json')
@app.route('/natural/moon/equatorial_radius_json', endpoint='/natural/moon/equatorial_radius_json')
def index():
    return render_template('json/natural/moon/equatorial_radius.json')
@app.route('/natural/moon/escape_velocity_json', endpoint='/natural/moon/escape_velocity_json')
def index():
    return render_template('json/natural/moon/escape_velocity.json')
@app.route('/natural/moon/length_of_day_json', endpoint='/natural/moon/length_of_day_json')
def index():
    return render_template('json/natural/moon/length_of_day.json')
@app.route('/natural/moon/mass_json', endpoint='/natural/moon/mass_json')
def index():
    return render_template('json/natural/moon/mass.json')
@app.route('/natural/moon/mean_density_json', endpoint='/natural/moon/mean_density_json')
def index():
    return render_template('json/natural/moon/mean_density.json')
@app.route('/natural/moon/mean_orbital_velocity_json', endpoint='/natural/moon/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/moon/mean_orbital_velocity.json')
@app.route('/natural/moon/orbital_period_json', endpoint='/natural/moon/orbital_period_json')
def index():
    return render_template('json/natural/moon/orbital_period.json')
@app.route('/natural/moon/polar_radius_json', endpoint='/natural/moon/polar_radius_json')
def index():
    return render_template('json/natural/moon/polar_radius.json')
@app.route('/natural/moon/solar_irradiance_json', endpoint='/natural/moon/solar_irradiance_json')
def index():
    return render_template('json/natural/moon/solar_irradiance.json')
@app.route('/natural/moon/surface_gravity_json', endpoint='/natural/moon/surface_gravity_json')
def index():
    return render_template('json/natural/moon/surface_gravity.json')
@app.route('/natural/moon/volume_json', endpoint='/natural/moon/volume_json')
def index():
    return render_template('json/natural/moon/volume.json')


"""Neptune"""
@app.route('/natural/neptune/axial_tilt_json', endpoint='/natural/neptune/axial_tilt_json')
def index():
    return render_template('json/natural/neptune/axial_tilt.json')
@app.route('/natural/neptune/black_body_temperature_json', endpoint='/natural/neptune/black_body_temperature_json')
def index():
    return render_template('json/natural/neptune/black_body_temperature.json')
@app.route('/natural/neptune/distance_from_sun_json', endpoint='/natural/neptune/distance_from_sun_json')
def index():
    return render_template('json/natural/neptune/distance_from_sun.json')
@app.route('/natural/neptune/equatorial_radius_json', endpoint='/natural/neptune/equatorial_radius_json')
def index():
    return render_template('json/natural/neptune/equatorial_radius.json')
@app.route('/natural/neptune/escape_velocity_json', endpoint='/natural/neptune/escape_velocity_json')
def index():
    return render_template('json/natural/neptune/escape_velocity.json')
@app.route('/natural/neptune/length_of_day_json', endpoint='/natural/neptune/length_of_day_json')
def index():
    return render_template('json/natural/neptune/length_of_day.json')
@app.route('/natural/neptune/mass_json', endpoint='/natural/neptune/mass_json')
def index():
    return render_template('json/natural/neptune/mass.json')
@app.route('/natural/neptune/mean_density_json', endpoint='/natural/neptune/mean_density_json')
def index():
    return render_template('json/natural/neptune/mean_density.json')
@app.route('/natural/neptune/mean_orbital_velocity_json', endpoint='/natural/neptune/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/neptune/mean_orbital_velocity.json')
@app.route('/natural/neptune/orbital_period_json', endpoint='/natural/neptune/orbital_period_json')
def index():
    return render_template('json/natural/neptune/orbital_period.json')
@app.route('/natural/neptune/polar_radius_json', endpoint='/natural/neptune/polar_radius_json')
def index():
    return render_template('json/natural/neptune/polar_radius.json')
@app.route('/natural/neptune/solar_irradiance_json', endpoint='/natural/neptune/solar_irradiance_json')
def index():
    return render_template('json/natural/neptune/solar_irradiance.json')
@app.route('/natural/neptune/surface_gravity_json', endpoint='/natural/neptune/surface_gravity_json')
def index():
    return render_template('json/natural/neptune/surface_gravity.json')
@app.route('/natural/neptune/volume_json', endpoint='/natural/neptune/volume_json')
def index():
    return render_template('json/natural/neptune/volume.json')


"""Saturn"""
@app.route('/natural/saturn/axial_tilt_json', endpoint='/natural/saturn/axial_tilt_json')
def index():
    return render_template('json/natural/saturn/axial_tilt.json')
@app.route('/natural/saturn/black_body_temperature_json', endpoint='/natural/saturn/black_body_temperature_json')
def index():
    return render_template('json/natural/saturn/black_body_temperature.json')
@app.route('/natural/saturn/distance_from_sun_json', endpoint='/natural/saturn/distance_from_sun_json')
def index():
    return render_template('json/natural/saturn/distance_from_sun.json')
@app.route('/natural/saturn/equatorial_radius_json', endpoint='/natural/saturn/equatorial_radius_json')
def index():
    return render_template('json/natural/saturn/equatorial_radius.json')
@app.route('/natural/saturn/escape_velocity_json', endpoint='/natural/saturn/escape_velocity_json')
def index():
    return render_template('json/natural/saturn/escape_velocity.json')
@app.route('/natural/saturn/length_of_day_json', endpoint='/natural/saturn/length_of_day_json')
def index():
    return render_template('json/natural/saturn/length_of_day.json')
@app.route('/natural/saturn/mass_json', endpoint='/natural/saturn/mass_json')
def index():
    return render_template('json/natural/saturn/mass.json')
@app.route('/natural/saturn/mean_density_json', endpoint='/natural/saturn/mean_density_json')
def index():
    return render_template('json/natural/saturn/mean_density.json')
@app.route('/natural/saturn/mean_orbital_velocity_json', endpoint='/natural/saturn/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/saturn/mean_orbital_velocity.json')
@app.route('/natural/saturn/orbital_period_json', endpoint='/natural/saturn/orbital_period_json')
def index():
    return render_template('json/natural/saturn/orbital_period.json')
@app.route('/natural/saturn/polar_radius_json', endpoint='/natural/saturn/polar_radius_json')
def index():
    return render_template('json/natural/saturn/polar_radius.json')
@app.route('/natural/saturn/solar_irradiance_json', endpoint='/natural/saturn/solar_irradiance_json')
def index():
    return render_template('json/natural/saturn/solar_irradiance.json')
@app.route('/natural/saturn/surface_gravity_json', endpoint='/natural/saturn/surface_gravity_json')
def index():
    return render_template('json/natural/saturn/surface_gravity.json')
@app.route('/natural/saturn/volume_json', endpoint='/natural/saturn/volume_json')
def index():
    return render_template('json/natural/saturn/volume.json')


"""Uranus"""
@app.route('/natural/uranus/axial_tilt_json', endpoint='/natural/uranus/axial_tilt_json')
def index():
    return render_template('json/natural/uranus/axial_tilt.json')
@app.route('/natural/uranus/black_body_temperature_json', endpoint='/natural/uranus/black_body_temperature_json')
def index():
    return render_template('json/natural/uranus/black_body_temperature.json')
@app.route('/natural/uranus/distance_from_sun_json', endpoint='/natural/uranus/distance_from_sun_json')
def index():
    return render_template('json/natural/uranus/distance_from_sun.json')
@app.route('/natural/uranus/equatorial_radius_json', endpoint='/natural/uranus/equatorial_radius_json')
def index():
    return render_template('json/natural/uranus/equatorial_radius.json')
@app.route('/natural/uranus/escape_velocity_json', endpoint='/natural/uranus/escape_velocity_json')
def index():
    return render_template('json/natural/uranus/escape_velocity.json')
@app.route('/natural/uranus/length_of_day_json', endpoint='/natural/uranus/length_of_day_json')
def index():
    return render_template('json/natural/uranus/length_of_day.json')
@app.route('/natural/uranus/mass_json', endpoint='/natural/uranus/mass_json')
def index():
    return render_template('json/natural/uranus/mass.json')
@app.route('/natural/uranus/mean_density_json', endpoint='/natural/uranus/mean_density_json')
def index():
    return render_template('json/natural/uranus/mean_density.json')
@app.route('/natural/uranus/mean_orbital_velocity_json', endpoint='/natural/uranus/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/uranus/mean_orbital_velocity.json')
@app.route('/natural/uranus/orbital_period_json', endpoint='/natural/uranus/orbital_period_json')
def index():
    return render_template('json/natural/uranus/orbital_period.json')
@app.route('/natural/uranus/polar_radius_json', endpoint='/natural/uranus/polar_radius_json')
def index():
    return render_template('json/natural/uranus/polar_radius.json')
@app.route('/natural/uranus/solar_irradiance_json', endpoint='/natural/uranus/solar_irradiance_json')
def index():
    return render_template('json/natural/uranus/solar_irradiance.json')
@app.route('/natural/uranus/surface_gravity_json', endpoint='/natural/uranus/surface_gravity_json')
def index():
    return render_template('json/natural/uranus/surface_gravity.json')
@app.route('/natural/uranus/volume_json', endpoint='/natural/uranus/volume_json')
def index():
    return render_template('json/natural/uranus/volume.json')


"""Venus"""
@app.route('/natural/venus/axial_tilt_json', endpoint='/natural/venus/axial_tilt_json')
def index():
    return render_template('json/natural/venus/axial_tilt.json')
@app.route('/natural/venus/black_body_temperature_json', endpoint='/natural/venus/black_body_temperature_json')
def index():
    return render_template('json/natural/venus/black_body_temperature.json')
@app.route('/natural/venus/distance_from_sun_json', endpoint='/natural/venus/distance_from_sun_json')
def index():
    return render_template('json/natural/venus/distance_from_sun.json')
@app.route('/natural/venus/equatorial_radius_json', endpoint='/natural/venus/equatorial_radius_json')
def index():
    return render_template('json/natural/venus/equatorial_radius.json')
@app.route('/natural/venus/escape_velocity_json', endpoint='/natural/venus/escape_velocity_json')
def index():
    return render_template('json/natural/venus/escape_velocity.json')
@app.route('/natural/venus/length_of_day_json', endpoint='/natural/venus/length_of_day_json')
def index():
    return render_template('json/natural/venus/length_of_day.json')
@app.route('/natural/venus/mass_json', endpoint='/natural/venus/mass_json')
def index():
    return render_template('json/natural/venus/mass.json')
@app.route('/natural/venus/mean_density_json', endpoint='/natural/venus/mean_density_json')
def index():
    return render_template('json/natural/venus/mean_density.json')
@app.route('/natural/venus/mean_orbital_velocity_json', endpoint='/natural/venus/mean_orbital_velocity_json')
def index():
    return render_template('json/natural/venus/mean_orbital_velocity.json')
@app.route('/natural/venus/orbital_period_json', endpoint='/natural/venus/orbital_period_json')
def index():
    return render_template('json/natural/venus/orbital_period.json')
@app.route('/natural/venus/polar_radius_json', endpoint='/natural/venus/polar_radius_json')
def index():
    return render_template('json/natural/venus/polar_radius.json')
@app.route('/natural/venus/solar_irradiance_json', endpoint='/natural/venus/solar_irradiance_json')
def index():
    return render_template('json/natural/venus/solar_irradiance.json')
@app.route('/natural/venus/surface_gravity_json', endpoint='/natural/venus/surface_gravity_json')
def index():
    return render_template('json/natural/venus/surface_gravity.json')
@app.route('/natural/venus/volume_json', endpoint='/natural/venus/volume_json')
def index():
    return render_template('json/natural/venus/volume.json')



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)