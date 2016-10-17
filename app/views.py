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
                        x=[properties_material['K_VRH_predicted'], properties_material['K_VRH']],
                        y=['Predict Bulk Modulus', 'Input Bulk Modulus'],
                        orientation='h'
                    ),
                    ],
                layout=dict(
                    title='first graph'
                    )
                )
            ]

        # Add "ids" to each of the graphs to pass up to the client
        # for templating
        ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

        # Get div of Plotly plot
        # pt_div = plotly.offline.plot(graph[0], show_link=False, output_type="div", include_plotlyjs=True)

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
