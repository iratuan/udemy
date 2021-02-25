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
    'https://raw.githubusercontent.com/iratuan/Udemy/master/Curso%20Dash%20Plotly/Data/gapminderDataFiveYear.csv')

years_option = []

for year in df['year'].unique():
    years_option.append({'label': str(year), 'value': year})

dropdown = dcc.Dropdown(id='year-picker',
                        options=years_option,
                        value=df['year'].min())

container_card = container('card mt-2 p-5',
                           container('form-group',
                                     [
                                         html.Label('Selecione o ano:'),
                                         dropdown,
                                         dcc.Graph(id='graph')
                                     ])
                           )

container_grafico = container('container',
                              container('col-md-12',
                                        container_card
                                        ))


app.layout = html.Div(className='pb-5',
                      children=[nav_bar,
                                container_grafico
                                ])


@app.callback(Output('graph', 'figure'),
              [Input(component_id='year-picker', component_property='value')])
def update_output_div(input_value):
    filtered_df = df[df['year'] == input_value]

    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']
                                      == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=continent_name
        ))

    return {'data': traces, 
            'layout': go.Layout(
                title='Espectativa de vida', 
                xaxis={'title': 'GDP Percapta', 'type': 'log'},
                yaxis={'title':'Life expectance'})}


if __name__ == '__main__':
    app.run_server(debug=True)
