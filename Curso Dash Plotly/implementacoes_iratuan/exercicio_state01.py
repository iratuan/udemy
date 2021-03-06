import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Div import Div
from dash.dependencies import Input, Output, State

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
                                    container('col-md-12',
                                              dcc.Input(id='number_in',
                                                        value=1,
                                                        className='form-control')),
                                    container('col-md-12 mt-5',
                                              html.Button(id='submit_button',
                                                          n_clicks=0,
                                                          children='Press me',
                                                          className='btn btn-lg btn-danger')),
                                    container('col-md-12 mt-5 alert alert-info',
                                              html.H1(id="number_out"))
                                ]),
                      ])


@app.callback(Output('number_out', 'children'),
              [Input(component_id='submit_button', component_property='n_clicks')],
              [State(component_id='number_in', component_property='value')])
def update_value(n_clicks, number):
    return '{} in and button was clicked {} times'.format(number, n_clicks)


app.layout = html.Div(className='pb-5',
                      children=[nav_bar, conteudo])


if __name__ == '__main__':
    app.run_server(debug=True)
