# --- IMPORTATION ---
import dash
import dash_bootstrap_components as dbc
from dash import html

# --- APP START ---
app = dash.Dash(__name__, use_pages=True, pages_folder="pages", external_stylesheets=[dbc.themes.SLATE]) #utilisaiton de plusieurs pages ainsi que d'un thème bootstrap 
    
server = app.server

    # --- COMPONENT CREATION ---
top_bar = dbc.Nav([dbc.NavLink([html.Div(page["name"])], href=page["path"], active="exact",className="button_page")for page in dash.page_registry.values()], vertical=False ,pills=True, className="top_bar")

title = html.H2("Colloc AgroBioTech", id="title_app", className="title_app")
    
bot_bar = html.H6("Date et heure ?",className="content_bot_bar")
    # --- APP CREATION ---
app.layout = html.Div([
    html.Div([
        title,
        top_bar],
        className="div_title_top_bar"),

    html.Div(dash.page_container,className="container"),

    html.Div([bot_bar],className="bot_bar")
],className="all_page"),



# --- APP START ---
if __name__ == "__main__":
    app.run_server(debug=True)


