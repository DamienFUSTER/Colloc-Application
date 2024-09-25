import dash
from dash import html

# --- PAGE DECLARATION ---
dash.register_page(module=__name__, name="Programme", path="/")

layout = html.Div([html.H1("Programme colloc"),
                   html.H5("nanan le programme")])
