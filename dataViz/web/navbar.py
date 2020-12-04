#
# Imports
#

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

nav = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Liste fichier", href="list")),
        dbc.NavItem(dbc.NavLink("Accueil", href="/")),
        dbc.NavItem(dbc.NavLink("Year", href="year")),
        dbc.NavItem(dbc.NavLink("Popular genres", href="popular_genres")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)