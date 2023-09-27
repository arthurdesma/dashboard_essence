import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd

# Importing required modules
from gas_station_density import generate_gas_station_density_map
from fuel_prices import generate_fuel_prices_map
from graph import update_gas_price_graph
from heat_map import generate_map, fuel_types

# Load data
df2 = pd.read_csv("prix-des-carburants-en-france-flux-instantane-v2.csv", delimiter=";", dtype={'Code postal': str})
departments = sorted(df2['Code postal'].astype(str).str[:2].unique())
options = [{'label': dept, 'value': dept} for dept in departments]

df1 = pd.read_csv('PrixCarburants_annuel_2022.csv')
grouped_df = df1.groupby(['Date', 'Gas_Type'])['Price'].mean().reset_index()

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

map_files = [generate_map(fuel) for fuel in fuel_types]

app.layout = dbc.Container([

    dbc.Row(html.H1("Gas Station Analysis in France", className="text-center mb-5"), className="mb-4"),

    dbc.Row(dbc.Col(dbc.Card(
        [
            dbc.CardHeader(html.H4("Fuel Prices by Department", className="card-title text-center")),
            dbc.CardBody([
                html.P("Choose a department to see average fuel prices. The map updates based on the selected department.", className="text-muted text-center mb-4"),
                dbc.Row(dbc.Col(dcc.Dropdown(id='department-dropdown', options=options, value='06', className="mb-3"), width=8), justify="center"),
                html.Iframe(id="fuel-prices-map", srcDoc=generate_fuel_prices_map('06'), width="100%", height="600", className="border-0")
            ])
        ]
    ), className="mb-4 shadow-sm")),

    dbc.Row([
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader(html.H4("Gas Station Density", className="card-title text-center")),
                dbc.CardBody([
                    html.P("This map shows the density of gas stations across France. Denser regions indicate more gas stations in that locality.", className="text-muted text-center mb-4"),
                    html.Iframe(id='gas-density-map', srcDoc=generate_gas_station_density_map(), width='100%', height='600', className="border-0")
                ])
            ]
        ), md=6, className="mb-4 shadow-sm"),

        dbc.Col(dbc.Card(
            [
                dbc.CardHeader(html.H4('Gas Price over Time', className="card-title text-center")),
                dbc.CardBody([
                    html.P("Select the gas type from the dropdown to view its average price trend over time.", className="text-muted text-center mb-4"),
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

    # Heat map section with card layout
    dbc.Row(dbc.Col(dbc.Card(
    [
        dbc.CardHeader(html.H4("Average Fuel Price per Department in France", className="card-title text-center")),
        dbc.CardBody(
            html.Div(
                [
                    html.Div(
                        [
                            html.H5(fuel.capitalize(), className="text-center mb-3"),
                            html.Iframe(srcDoc=open(map_file, 'r').read(), width='100%', height='600', className="border-0")
                        ],
                        className="mb-4",
                        style={"width": "33%", "height": "600px"}  # Here we're setting the size of each map's container.
                    )
                    #zip() = combine 2 lists
                    for fuel, map_file in zip(fuel_types, map_files)
                ],
                style={"display": "flex", "flexDirection": "row", "flexWrap": "wrap", "justifyContent": "space-between"}
            )
        )
    ]
), className="mb-4 shadow-sm"))


], fluid=True, className="mt-4 p-4")

# Callbacks
@app.callback(
    Output('fuel-prices-map', 'srcDoc'),
    [Input('department-dropdown', 'value')]
)
def update_map(selected_department):
    return generate_fuel_prices_map(selected_department)

@app.callback(
    Output('line-plot', 'figure'),
    [Input('gas-type-dropdown', 'value')]
)
def update_graph(selected_gas_type):
    return update_gas_price_graph(selected_gas_type)

# Main
if __name__ == '__main__':
    app.run_server(debug=True)
