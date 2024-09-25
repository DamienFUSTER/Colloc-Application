import dash
from dash import html

# --- PAGE DECLARATION ---
dash.register_page(module=__name__, name="Liens utiles")

layout = html.Div([html.H1("Liens utiles"),
                   html.H5("nanan les liens utiles")])
