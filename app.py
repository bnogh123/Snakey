"""
Snakey - Interactive Snake Dashboard
Main application entry point
"""

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

# Server instance for deployment
server = app.server

# Navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("US Overview", href="/")),
        dbc.NavItem(dbc.NavLink("Global View", href="/global")),
        dbc.NavItem(dbc.NavLink("Domesticated Snakes", href="/domesticated")),
        dbc.NavItem(dbc.NavLink("Snakes in Media", href="/media")),
        dbc.NavItem(dbc.NavLink("Farming Ethics", href="/farming")),
    ],
    brand="Snakey Dashboard",
    brand_href="/",
    color="dark",
    dark=True,
    fluid=True,
)

# App layout with URL routing
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', style={'padding': '20px'})
])

# Callback for page routing
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    """Route to different pages based on URL"""
    if pathname == '/':
        from src.pages import us_overview
        return us_overview.layout
    elif pathname == '/global':
        from src.pages import global_view
        return global_view.layout
    elif pathname == '/domesticated':
        from src.pages import domesticated
        return domesticated.layout
    elif pathname == '/media':
        from src.pages import media
        return media.layout
    elif pathname == '/farming':
        from src.pages import farming
        return farming.layout
    else:
        return html.Div([
            html.H1("404: Page not found", className="text-center"),
            html.P("The page you're looking for doesn't exist.", className="text-center")
        ])

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8050)
