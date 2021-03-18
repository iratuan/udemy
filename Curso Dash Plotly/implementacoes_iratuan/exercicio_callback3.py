import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Label import Label
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

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
    'https://raw.githubusercontent.com/iratuan/Udemy/master/Curso%20Dash%20Plotly/Data/mpg.csv')

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
                                    container('col-md-6', ddx),
                                    container('col-md-6', ddy),
                                ]),
                      container('row',
                                container('col-md-12', dcc.Graph(id='graph')))
                      ])


app.layout = html.Div(className='pb-5',
                      children=[nav_bar, conteudo])


@app.callback(Output('graph', 'figure'),
              [Input(component_id='xaxis', component_property='value'),
               Input(component_id='yaxis', component_property='value')])
def update_output_div(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {
                    'width': 0.5, 'color': 'white'
                }
            }
        )],
        'layout': go.Layout(
            title='Features',
            xaxis={'title': xaxis_name},
            yaxis={'title': yaxis_name})
    }


if __name__ == '__main__':
    app.run_server(debug=True)
