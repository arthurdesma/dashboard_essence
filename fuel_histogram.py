# fuel_histogram.py
import pandas as pd
import plotly.graph_objs as go

def generate_fuel_histogram(df2):

    # Extract the price columns for different fuel types
    gazole_prices = df2["Gazole_prix"]
    sp95_prices = df2["SP95_prix"]
    e85_prices = df2["E85_prix"]
    gplc_prices = df2["GPLc_prix"]
    e10_prices = df2["E10_prix"]
    sp98_prices = df2["SP98_prix"]

    trace1 = go.Histogram(x=gazole_prices, name='Gazole', opacity=0.5)
    trace2 = go.Histogram(x=sp95_prices, name='SP95', opacity=0.5)
    trace3 = go.Histogram(x=e85_prices, name='E85', opacity=0.5)
    trace4 = go.Histogram(x=gplc_prices, name='GPLc', opacity=0.5)
    trace5 = go.Histogram(x=e10_prices, name='E10', opacity=0.5)
    trace6 = go.Histogram(x=sp98_prices, name='SP98', opacity=0.5)

    layout = go.Layout(
        title='Fuel Price Histogram',
        xaxis={'title': 'Price'},
        yaxis={'title': 'Frequency'},
        barmode='overlay'
    )

    fig = go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6], layout=layout)

    return fig
