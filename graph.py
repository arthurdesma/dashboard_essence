import pandas as pd
import plotly.express as px


def update_gas_price_graph(selected_gas_type,df1):
    grouped_df = df1.groupby(['Date', 'Gas_Type'])['Price'].mean().reset_index()
    
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