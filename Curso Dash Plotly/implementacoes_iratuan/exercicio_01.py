import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

# external JavaScript files
external_scripts = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js',
    'https://code.jquery.com/jquery-3.5.1.min.js'
]


# external CSS stylesheets
external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']


app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

# Creating Data

np.random.seed(42)

randon_x = np.random.randint(1, 101, 100)
randon_y = np.random.randint(1, 101, 100)


# <div class="card">
#   <div class="card-header">
#     Featured
#   </div>
#   <div class="card-body">
#     <h5 class="card-title">Special title treatment</h5>
#     <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
#     <a href="#" class="btn btn-primary">Go somewhere</a>
#   </div>
# </div>

# <nav class="navbar navbar-light bg-light">
#   <span class="navbar-brand mb-0 h1">Navbar</span>
# </nav>

# html.Nav(
#     className='navbar navbar-light bg-light',
#     children=html.Span(
#         className='navbar-brand mb-0 h1',
#         children='Meu dashboard'
#     )
# )

app.layout = html.Div(className='pb-5',
                      children=[
                          html.Nav(
                              className='navbar navbar-dark bg-danger',
                              children=html.Span(
                                  className='navbar-brand mb-0 h1',
                                  children='Meu dashboard'
                              )
                          ),
                          html.Div(className='container',
                                   children=html.Div(className='row mt-5',
                                                     children=[html.Div(className='col-md-6',
                                                                        children=html.Div(className='card',
                                                                                          children=[
                                                                                              html.Div(
                                                                                                  className='card-header',
                                                                                                  children='Meu gráfico muito massa'
                                                                                              ),
                                                                                              html.Div(
                                                                                                  className='card-body',
                                                                                                  children=[
                                                                                                      html.H5(
                                                                                                          'Amostragem legal'),
                                                                                                      html.P(
                                                                                                          'Aqui fica a descrição toda da coisa'),
                                                                                                      dcc.Graph(
                                                                                                          id='scatterplot1',
                                                                                                          figure={
                                                                                                             'data': [
                                                                                                                 go.Scatter(
                                                                                                                     x=randon_x,
                                                                                                                     y=randon_y,
                                                                                                                     name='Meus dados',
                                                                                                                     mode='markers'
                                                                                                                 )
                                                                                                             ],
                                                                                                              'layout': go.Layout(
                                                                                                                 title='Meu gráfico'
                                                                                                             )}
                                                                                                      )
                                                                                                  ]
                                                                                              )
                                                                                          ])
                                                                        ), html.Div(className='col-md-6',
                                                                                    children=html.Div(className='card',
                                                                                                      children=[
                                                                                                          html.Div(
                                                                                                              className='card-header',
                                                                                                              children='Meu gráfico muito massa'
                                                                                                          ),
                                                                                                          html.Div(
                                                                                                              className='card-body',
                                                                                                              children=[
                                                                                                                  html.H5(
                                                                                                                      'Amostragem legal'),
                                                                                                                  html.P(
                                                                                                                      'Aqui fica a descrição toda da coisa'),
                                                                                                                  dcc.Graph(
                                                                                                                      id='scatterplot2',
                                                                                                                      figure={
                                                                                                                          'data': [
                                                                                                                              go.Scatter3d(
                                                                                                                                  x=randon_x,
                                                                                                                                  y=randon_y,
                                                                                                                                  z=randon_x,
                                                                                                                                  name='Meus dados',
                                                                                                                                  mode='markers'
                                                                                                                              )
                                                                                                                          ],
                                                                                                                          'layout': go.Layout(
                                                                                                                              title='Meu gráfico'
                                                                                                                          )}
                                                                                                                  )
                                                                                                              ]
                                                                                                          )
                                                                                                      ])
                                                                                    )]
                                                     )
                                   )
                      ])


if __name__ == '__main__':
    app.run_server(debug=True)
