#
# Imports
#

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

class Server:

    def __configure_server(self):

        app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

        navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Liste fichier", href="#")),
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

        app.layout = html.Div(
            children=[
                navbar,
            ]
        )

        return app

    def run_server(self):
        app = self.__configure_server()
        app.run_server(debug=True)  # (8)