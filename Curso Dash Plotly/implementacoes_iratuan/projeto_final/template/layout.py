import dash_html_components as html


# external JavaScript files
external_scripts = [
    'https://code.jquery.com/jquery-3.5.1.min.js',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'
]


# external CSS stylesheets
external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']


nav_bar = html.Nav(
    className='navbar navbar-dark bg-danger',
    children=html.Div(
        className='container',
        children=html.Span(
            className='navbar-brand mb-0 h1',
            children='Meu dashboard'
        )
    )
)


header = html.Header()

footer = html.Footer()


def container(estilo, conteudo):
    return (
        html.Div(className=estilo,
                 children=conteudo
                 )
    )


def card(titulo, conteudo):
    return(html.Div(className='card',
                    children=[
                        html.Div(
                            className='card-header',
                            children=titulo
                        ),
                        html.Div(
                            className='card-body',
                            children=conteudo)

                    ])
           )
