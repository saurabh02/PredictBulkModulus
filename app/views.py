from flask import render_template, redirect, request
from app import app, models, db
from .forms import MaterialForm
from models import display


@app.route('/')
def index():
    return redirect('/select_material')


@app.route('/select_material', methods=['GET', 'POST'])
def select_material():
    form = MaterialForm()
    if form.validate_on_submit():
        material_formula = form.formula.data
        properties_material = display(material_formula)
        print properties_material['K_VRH_predicted']
        return render_template('home.html', properties_material=properties_material, material_name=material_formula)
        # return redirect('/properties/')
    return render_template('material.html', form=form)

# @app.route('/properties/<value>')
# def properties(value):
#     properties_material = display(value)
#     print properties_material
#     return render_template('home.html',
#                             properties_material=properties_material)
