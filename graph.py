import pandas as pd
import plotly.express as px
from xml_to_csv import parse_xml_to_csv

#parse_xml_to_csv()

df1 = pd.read_csv('PrixCarburants_annuel_2022.csv')
grouped_df = df1.groupby(['Date', 'Gas_Type'])['Price'].mean().reset_index()

def update_gas_price_graph(selected_gas_type):
    filtered_df = grouped_df[grouped_df['Gas_Type'] == selected_gas_type]
    fig = px.line(filtered_df, x='Date', y='Price', title=f'Price of {selected_gas_type} over Time')
    fig.update_layout(
        title_font=dict(size=24, color='#4CAF50'),
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_showgrid=False,
        yaxis_showgrid=True,
        yaxis_gridcolor='#E0E0E0',
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    return fig
