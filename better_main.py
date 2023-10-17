import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd

# Importation des modules nécessaires
from gas_station_density import generate_gas_station_density_map
from fuel_prices import generate_fuel_prices_map
from graph import update_gas_price_graph
from heat_map import generate_map, fuel_types
from fuel_histogram import generate_fuel_histogram


# Charger les données
df2 = pd.read_csv("prix-des-carburants-en-france-flux-instantane-v2.csv", delimiter=";", dtype={'Code postal': str})
departements = sorted(df2['Code postal'].astype(str).str[:2].unique())
options = [{'label': dept, 'value': dept} for dept in departements]

df1 = pd.read_csv('PrixCarburants_annuel_2022.csv')
grouped_df = df1.groupby(['Date', 'Gas_Type'])['Price'].mean().reset_index()

# Initialiser l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

map_files = [generate_map(fuel) for fuel in fuel_types]

app.layout = dbc.Container([

    dbc.Row(html.H1("Analyse des stations-service en France", className="text-center mb-5"), className="mb-4"),

    dbc.Row(dbc.Col(dbc.Card(
        [
            dbc.CardHeader(html.H4("Prix du carburant par département", className="card-title text-center")),
            dbc.CardBody([
                html.P("Choisissez un département pour voir les prix moyens du carburant. La carte se met à jour selon le département sélectionné.", className="text-muted text-center mb-4"),
                dbc.Row(dbc.Col(dcc.Dropdown(id='department-dropdown', options=options, value='06', className="mb-3"), width=8), justify="center"),
                html.Iframe(id="fuel-prices-map", srcDoc=generate_fuel_prices_map('06'), width="100%", height="600", className="border-0")
            ])
        ]
    ), className="mb-4 shadow-sm")),

    dbc.Row([
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader(html.H4("Densité des stations-service", className="card-title text-center")),
                dbc.CardBody([
                    html.P("Cette carte montre la densité des stations-service à travers la France. Les régions plus denses indiquent un plus grand nombre de stations-service dans cette localité.", className="text-muted text-center mb-4"),
                    html.Iframe(id='gas-density-map', srcDoc=generate_gas_station_density_map(), width='100%', height='600', className="border-0")
                ])
            ]
        ), md=6, className="mb-4 shadow-sm"),

        dbc.Col(dbc.Card(
            [
                dbc.CardHeader(html.H4('Prix du carburant au fil du temps', className="card-title text-center")),
                dbc.CardBody([
                    html.P("Sélectionnez le type de carburant dans le menu déroulant pour voir son évolution de prix moyenne au fil du temps.", className="text-muted text-center mb-4"),
                    dcc.Dropdown(
                        id='gas-type-dropdown',
                        options=[{'label': gas_type, 'value': gas_type} for gas_type in grouped_df['Gas_Type'].unique()],
                        value='Gazole',
                        clearable=False,
                        className="mb-3"
                    ),
                    dcc.Graph(id='line-plot')
                ])
            ]
        ), md=6, className="shadow-sm")
    ], className="mb-4"),
    
    # Section de la carte thermique avec mise en page de la carte
    dbc.Row(dbc.Col(dbc.Card(
    [
        dbc.CardHeader(html.H4("Prix moyen du carburant par département en France", className="card-title text-center")),
        dbc.CardBody(
            html.Div(
                [
                    html.Div(
                        [
                            html.H5(fuel.capitalize(), className="text-center mb-3"),
                            html.Iframe(srcDoc=generate_map(fuel).get_root().render(), width='100%', height='600', className="border-0")
                        ],
                        className="mb-4",
                        style={"width": "33%", "height": "600px"}
                    )
                    for fuel in fuel_types
                ],
                style={"display": "flex", "flexDirection": "row", "flexWrap": "wrap", "justifyContent": "space-between"}
                )
            )
    ]
), className="mb-4 shadow-sm"),),
    
    dbc.Row(dbc.Col(dbc.Card(
        [
            dbc.CardHeader(html.H4('Histogramme des prix des carburants', className="card-title text-center")),
            dbc.CardBody([
                html.P("Cet histogramme montre la distribution des prix des différents types de carburants.", className="text-muted text-center mb-4"),
                dcc.Graph(figure=generate_fuel_histogram())
            ])
        ]
    ), className="mb-4 shadow-sm"))
    

], fluid=True, className="mt-4 p-4")

# Callbacks
@app.callback(
    Output('fuel-prices-map', 'srcDoc'),
    [Input('department-dropdown', 'value')]
)
def update_map(departement_selectionne):
    return generate_fuel_prices_map(departement_selectionne)

@app.callback(
    Output('line-plot', 'figure'),
    [Input('gas-type-dropdown', 'value')]
)
def update_graph(type_carburant_selectionne):
    return update_gas_price_graph(type_carburant_selectionne)

# Principal
if __name__ == '__main__':
    app.run_server(debug=True)
