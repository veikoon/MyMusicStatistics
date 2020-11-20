#
# Imports
#

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from web.navbar import nav
from get_metadata import GetMetadata

layout_home = html.Div(
    children=[
        nav,
    ]
)
