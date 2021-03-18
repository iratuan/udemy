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


df = pd.read_csv(
    'https://raw.githubusercontent.com/iratuan/Udemy/master/Curso%20Dash%20Plotly/exemplos/Data/wheels.csv')

features = df.columns

ddx = dcc.Dropdown(id='xaxis',
                   options=[{'label': i, 'value': i} for i in features],
                   value='displacement')
ddy = dcc.Dropdown(id='yaxis',
                   options=[{'label': i, 'value': i} for i in features],
                   value='mpg')

conteudo = container('container p-5',
                     [container('row',
                                [
                                    html.Div(className="row m-5", children=[
                                        dcc.RadioItems(id="wheels",
                                                       options=[{'label': i, 'value': i}
                                                                for i in df['wheels'].unique()],
                                                       value=1),
                                        html.Div(id="wheels-output",
                                                 className="alert alert-info"),
                                    ]),
                                    html.Div(className="row m-5", children=[
                                        dcc.RadioItems(id="colors",
                                                       options=[{'label': i, 'value': i}
                                                                for i in df['color'].unique()],
                                                       value='blue'),
                                        html.Div(id="colors-output",
                                                 className="alert alert-info"),
                                    ]),
                                    html.Img(id='display-image',
                                             src='children', height=300),

                                ]),
                      ])


app.layout = html.Div(className='pb-5',
                      children=[nav_bar, conteudo])


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


@app.callback(
    Output('display-image', 'src'),
    [Input('wheels', 'value'),
     Input('colors', 'value')])
def callback_image(wheel, color):
    path = 'images/'
    return encode_image(path+df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0])


@app.callback(Output('wheels-output', 'children'),
              [Input(component_id='wheels', component_property='value')])
def callback_a(wheels_value):
    return "Voce escolheu {}".format(wheels_value)


@app.callback(Output('colors-output', 'children'),
              [Input(component_id='colors', component_property='value')])
def callback_a(colors_value):
    return "Voce escolheu {}".format(colors_value)


if __name__ == '__main__':
    app.run_server(debug=True)
