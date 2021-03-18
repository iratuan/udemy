import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader as web
from datetime import datetime
import dash_bootstrap_components as dbc


from template import layout as l


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


nav_bar = l.nav_bar

app.layout = html.Div([nav_bar,
                       l.container('container',
                                   [l.container('row mt-5',
                                                l.container('col-md-12',
                                                            html.H3(
                                                                'Stock ticker dashboard')
                                                            )
                                                ),
                                    l.container('row mt-2', [
                                        l.container('col-md-6',
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [html.H6(
                                                                'Select', className="card-title"),
                                                                dcc.Input(
                                                                    id='my_stock_picker',
                                                                    value='TSLA',
                                                                    className='form-control')]
                                                        ),
                                                        className="mb-3")
                                                    )

                                    ]),
                                       l.container('row',
                                                   l.container('col-md-12 mt-2',
                                                               l.card('Stock ticker',
                                                                      dcc.Graph(id='my_graph', figure={
                                                                          'data': [{'x': [1, 2], 'y':[3, 1]}],
                                                                          'layout': {'title': 'Default title'}
                                                                      }))
                                                               ),
                                                   )
                                    ])
                       ])


# FUNCTIONS
@app.callback(Output('my_graph', 'figure'),
              [Input('my_stock_picker', 'value')])
def update_graph(stock_ticker):
    start = datetime(2017, 1, 1)
    end = datetime(2021, 2, 28)
    df = web.DataReader(stock_ticker,'iex',start,end)
    fig = {
        'data': [{'x': df.index, 'y':df['close']}],
        'layout': {'title': stock_ticker}
    }

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
