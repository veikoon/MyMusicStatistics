import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'custom_style.css'
        ]
    )

nav = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Music list", href="list")),
        dbc.NavItem(dbc.NavLink("Year", href="year")),
        dbc.NavItem(dbc.NavLink("Popular genres", href="popular_genres")),
        dbc.NavItem(dbc.NavLink("Average genre duration", href="average_genre_duration")),
    ],
    brand="Music Statistics",
    brand_href="#",
    color="primary",
    dark=True,
)