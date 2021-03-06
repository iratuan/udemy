import dash
import dash_core_components as dcc
from dash_core_components.RadioItems import RadioItems
import dash_html_components as html
from dash_html_components.Div import Div
from dash_html_components.Label import Label
from pandas.core import base
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import base64

from navbar import nav_bar


# external JavaScript files
external_scripts = [
    'https://code.jquery.com/jquery-3.5.1.min.js',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'
]


# external CSS stylesheets
external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']


app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)


nav_bar = nav_bar


def container(estilo, conteudo):
    return (
        html.Div(className=estilo,
                 children=conteudo
                 )
    )


conteudo = container('container p-5',
                     [container('row',
                                [
                                    container('col-md-12', dcc.RangeSlider(
                                        id="range-slide",
                                        min=-10,
                                        max=10,
                                        marks={i: str(i)
                                               for i in range(-10, 10)},
                                        value=[-1, 1]
                                    )),
                                    container('col-md-12 alert alert-info',html.H1(id="produto"))
                                ]),
                      ])

@app.callback(Output('produto', 'children'),
              [Input(component_id='range-slide', component_property='value')])
def update_value(value_list):
    return value_list[0] * value_list[1]


app.layout = html.Div(className='pb-5',
                      children=[nav_bar, conteudo])


if __name__ == '__main__':
    app.run_server(debug=True)
