import pandas as pd
import folium
from folium.plugins import MarkerCluster

def generate_fuel_prices_map(df2,selected_department='06'):
    # Load data from the CSV file
    df2 = pd.read_csv("data/prix-des-carburants-en-france-flux-instantane-v2.csv", delimiter=";", dtype={'Code postal': str})
    df2 = df2.drop(columns=['latitude', 'longitude'])

    filtered_df = df2[df2['Code postal'].astype(str).str.startswith(selected_department)]
    
    def compute_centroid(dataframe):
        """Computes the centroid of given dataframe."""
        lats, lons = [], []
        for _, row in dataframe.iterrows():
            lat, lon = map(float, row['geom'].split(','))
            lats.append(lat)
            lons.append(lon)
        return sum(lats) / len(lats), sum(lons) / len(lons)
    
    center = compute_centroid(filtered_df)
    m = folium.Map(location=center, zoom_start=10)

    
    fuel_types = [col.split('_')[0] for col in filtered_df.columns if "_maj" in col]
    feature_groups = {}
    clusters = {}

    for fuel in fuel_types:
        feature_groups[fuel] = folium.FeatureGroup(name=fuel)
        clusters[fuel] = MarkerCluster().add_to(feature_groups[fuel])

    for index, row in filtered_df.iterrows():
        lat, lon = map(float, row['geom'].split(','))

        description = (f"<b>Address:</b> {row['Adresse']}<br>"
                       f"<b>City:</b> {row['Ville']}<br>"
                       f"<b>Available Fuels:</b> {row['Carburants disponibles']}<br>")

        for fuel in fuel_types:
            price_col = f"{fuel}_prix"
            maj_col = f"{fuel}_maj"

            if not pd.isna(row[maj_col]):
                fuel_details = (f"<b>prix {fuel}:</b> {row[price_col]}<br>"
                                f"mise a jour le: {row[maj_col]}<br>")
                description += fuel_details

                folium.Marker([lat, lon], tooltip=row['Ville'], popup=description).add_to(clusters[fuel])

    for fuel, group in feature_groups.items():
        group.add_to(m)

    folium.LayerControl().add_to(m)

    return m._repr_html_()