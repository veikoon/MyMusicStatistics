#
# Imports
#

import dash_html_components as html
from web.navbar import nav

class Home:
    
    def getLayout():

        layout_home = html.Div(
            children=[
                nav,
            ]
        )

        return layout_home
