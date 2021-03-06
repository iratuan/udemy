import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output, State
import json
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


df = pd.read_csv(
    'https://raw.githubusercontent.com/iratuan/Udemy/master/Curso%20Dash%20Plotly/exemplos/Data/wheels.csv')


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
                                    container('col-md-6',
                                              dcc.Graph(
                                                  id='wheels-plot',
                                                  figure={'data': [go.Scatter(
                                                      x=df['color'],
                                                      y=df['wheels'],
                                                      dy=1,
                                                      
                                                      mode='markers',
                                                      marker={
                                                          'size': 15
                                                      }
                                                  )], 'layout': go.Layout(
                                                      title='Test',
                                                      hovermode='closest'
                                                  )}
                                              )),
                                    container('col-md-6',
                                              html.Img(
                                                  id='hover-image',
                                                  src='children',
                                                  height=300
                                              ))
                                ]),
                      ])


@app.callback(
    Output('hover-image', 'src'),
    [Input('wheels-plot', 'hoverData')])
def callback_image(hoverData):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = 'Images/'
    return encode_image(path+df[(df['wheels'] == wheel) &
                                (df['color'] == color)]['image'].values[0])


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


app.layout = html.Div(className='pb-5',
                      children=[nav_bar, conteudo])


if __name__ == '__main__':
    app.run_server(debug=True)
