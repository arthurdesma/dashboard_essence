# main.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from gas_station_density import generate_gas_station_density_map
from fuel_prices import generate_fuel_prices_map
from graph import update_gas_price_graph
from heat_map import get_heat_map_layout  # Import the heat map layout function

# Load data for dropdown
df2 = pd.read_csv("prix-des-carburants-en-france-flux-instantane-v2.csv", delimiter=";", dtype={'Code postal': str})
departments = sorted(df2['Code postal'].astype(str).str[:2].unique())
options = [{'label': dept, 'value': dept} for dept in departments]

df1 = pd.read_csv('PrixCarburants_annuel_2022.csv')
grouped_df = df1.groupby(['Date', 'Gas_Type'])['Price'].mean().reset_index()

app = dash.Dash(__name__)

layout_gas_price = html.Div([
    html.H1('Gas Price over Time', style={'textAlign': 'center', 'color': '#4CAF50'}),
    dcc.Dropdown(
        id='gas-type-dropdown',
        options=[{'label': gas_type, 'value': gas_type} for gas_type in grouped_df['Gas_Type'].unique()],
        value='Gazole',
        clearable=False,
        style={'width': '50%', 'margin': '0 auto'}
    ),
    dcc.Graph(id='line-plot')
])

app.layout = html.Div([
    html.H1("Gas Station Density in France"),
    html.Iframe(id='gas-density-map', srcDoc=generate_gas_station_density_map(), width='100%', height='600'),
    html.H1("Fuel Prices in France"),
    dcc.Dropdown(id='department-dropdown', options=options, value='06'),
    html.Iframe(id="fuel-prices-map", srcDoc=generate_fuel_prices_map('06'), width="100%", height="600"),
    layout_gas_price,
    get_heat_map_layout()  # Add the heat map layout to the main layout
])

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

if __name__ == '__main__':
    app.run_server(debug=True)
