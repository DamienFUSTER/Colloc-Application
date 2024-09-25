import dash
from dash import html

# --- PAGE DECLARATION ---
dash.register_page(module=__name__, name="Présentation")

layout = html.Div([html.H1("Présentation intervenant"),
                   html.H5("nanan la prez des gens")])
