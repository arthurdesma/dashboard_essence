import geopandas as gpd
import folium

def generate_gas_station_density_map(df2):
    # Make a copy of the dataframe to avoid modifying the original data
    df_copy = df2.copy()

    # Extract the first two digits from the 'Code postal' column
    df_copy['Dept_code'] = df_copy['Code postal'] // 1000  # Integer division by 1000 to get the first two digits.

    # Read the geojson file
    gdf_departements = gpd.read_file('data/departements.geojson')

    # Group by 'Dept_code' to count the number of gas stations per department code
    gas_station_density = df_copy.groupby('Dept_code').size().reset_index(name='count')

    # Merge with the geojson file
    gdf_departements['code'] = gdf_departements['code'].replace({'2A': '20', '2B': '20'}).astype(int)
    merged = gdf_departements.set_index('code').join(gas_station_density.set_index('Dept_code'))

    m = folium.Map([46.603354, 1.888334], zoom_start=6)  # Center on France

    # Visualize the gas station density
    folium.Choropleth(
        geo_data=merged,
        name='choropleth',
        data=merged,
        columns=[merged.index, 'count'],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Gas Station Density'
    ).add_to(m)

    return m._repr_html_()
