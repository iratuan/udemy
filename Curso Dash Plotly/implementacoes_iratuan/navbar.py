import dash_html_components as html

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
