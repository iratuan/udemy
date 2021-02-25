import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from navbar import nav_bar

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')

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


grafico = dcc.Graph(
    id='scatterplot1',
    figure={
        'data': [
            go.Scattergeo(
                locationmode='USA-states',
                lon=df['lon'],
                lat=df['lat'],
                text=df['name'] + '- População: ' + df['pop'].astype(
                    str),
                marker=dict(
                    size=df['pop'] /
                    5000,
                    color='#e74c3c',
                    line={'width': 0.5,
                          'color': '#2c3e50'},
                    sizemode='area')
            )
        ],
        'layout': go.Layout(
            title='<b>População americana em 2014</b>',
            titlefont={'family': 'Arial',
                       'size': 24},
            geo={'scope': 'usa',
                 'projection': {'type': 'albers usa'},
                 'showland': True,
                 'landcolor': '#2ecc71',
                 'showlakes': True,
                 'lakecolor': '#3498db',
                 'subunitwidth': 1,
                 'subunitcolor': "rgb(255, 255, 255)",
                 },
            height=600,
            width=960)
    }
)

container_card = container('card mt-2',
                           container('grafico',
                                     [grafico]
                                     ))

container_grafico = container('container',
                              container('col-md-12',
                                        container_card
                                        ))


app.layout = html.Div(className='pb-5',
                      children=[nav_bar,
                                container_grafico
                                ])


if __name__ == '__main__':
    app.run_server(debug=True)
