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