import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Label import Label
import plotly.graph_objects as go
from dash.dependencies import Input, Output

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


input = dcc.Input(id='my-input', value='valor inicial',
                  type='text', className='form-control')

container_card = container('card mt-2 p-5',
                           container('form-group',
                                     [
                                         html.Label('Digite algo'),
                                         input,
                                         html.Div(id='my-div', className='alert alert-danger mt-5', role='alert')]
                                     ))

container_grafico = container('container',
                              container('col-md-12',
                                        container_card
                                        ))


app.layout = html.Div(className='pb-5',
                      children=[nav_bar,
                                container_grafico
                                ])

@app.callback(Output(
    component_id='my-div',
    component_property='children'
),[Input(component_id='my-input', component_property='value')])
def update_output_div(input_value):
    return 'Voce digitou {} '.format(input_value)



if __name__ == '__main__':
    app.run_server(debug=True)
