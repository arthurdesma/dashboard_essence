import pandas as pd
import geopandas as gpd
import folium

# Load the required data.
df = pd.read_csv('prix-des-carburants-en-france-flux-instantane-v2.csv', delimiter=";")
df['Dept_code'] = df['Code postal'] // 1000

gdf_departements = gpd.read_file('departements.geojson')
gdf_departements['code'] = gdf_departements['code'].replace({'2A': '20', '2B': '20'}).astype(int)

fuel_types = [col.replace('_prix', '') for col in df.columns if '_prix' in col][:6]

# Define a function to generate a map based on the provided fuel type.
def generate_map(fuel_type):
    avg_price_per_dept = df.groupby('Dept_code')[f'{fuel_type}_prix'].mean().reset_index(name='avg_price')
    merged = gdf_departements.set_index('code').join(avg_price_per_dept.set_index('Dept_code'))
    m = folium.Map([46.603354, 1.888334], zoom_start=5)
    folium.Choropleth(
        geo_data=merged, name='choropleth', data=merged,
        columns=[merged.index, 'avg_price'], key_on='feature.id',
        fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
        legend_name=f'Average {fuel_type} Price in €'
    ).add_to(m)
    m.save(f'avg_{fuel_type}_price_per_department.html')
    return f'avg_{fuel_type}_price_per_department.html'
