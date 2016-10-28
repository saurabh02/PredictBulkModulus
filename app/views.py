from flask import render_template, redirect, request
from app import app, models
from .forms import MaterialForm
from models import display
import plotly.graph_objs as go
import json
import plotly


@app.route('/')
def index():
    return redirect('/select_material')
    # return render_template('index.html')


@app.route('/index')
def template():
    return redirect('/select_material')


@app.route('/select_material', methods=['GET', 'POST'])
def select_material():
    form = MaterialForm()
    if form.validate_on_submit():
        material_formula = form.formula.data
        properties_material = display(material_formula)
        graphs = [
            dict(
                data=[
                    go.Bar(
                        # x=[properties_material['K_VRH'], properties_material['K_VRH_predicted']],
                        x=[properties_material[0][1], properties_material[0][15]],
                        y=['MP value', 'Predicted value'],
                        orientation='h'
                    ),
                    ],
                layout=dict(
                    title='Calculated v/s predicted Bulk modulus',
                    xaxis=dict(title='Bulk modulus (GPa)'),
                    margin=dict(l=175, t=175, b=150, r=175)
                    )
                )
            ]

        # Add "ids" to each of the graphs to pass up to the client
        # for templating
        ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

        # Convert the figures to JSON
        # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
        # objects to their JSON equivalents
        graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('results.html', properties_material=properties_material, material_name=material_formula,
                               ids=ids, graphJSON=graphJSON)
        # return redirect('/properties/')
    return render_template('material.html', form=form)


# @app.route('/properties/<value>')
# def properties(value):
#     properties_material = display(value)
#     print properties_material
#     return render_template('home.html',
#                             properties_material=properties_material)
