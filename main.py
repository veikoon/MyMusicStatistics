#
# Imports
#

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

#
# Main
#


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
children=[
    dbc.NavItem(dbc.NavLink("Page 1", href="#")),
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

#
# RUN APP
#
if __name__ == '__main__':

    app.run_server(debug=True) # (8)