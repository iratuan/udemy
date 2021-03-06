import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

pagina_home = html.Div('Home page')

pagina_contato = html.Div('Contato page')

app.layout = html.Div([
    dcc.Dropdown(id='paginas', options=[{'label': 'home', 'value': 'home'}, {
        'label': 'contato', 'value': 'contato'}], value='home'),
    html.Div(id='container')
])


@app.callback(Output('container', 'children'),
              [Input('paginas', 'value')])
def seleciona_pagina(pagina):
    if(pagina == 'home'):
        return pagina_home
    else:
        return pagina_contato


if __name__ == '__main__':
    app.run_server(debug=True)
