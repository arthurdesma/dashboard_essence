import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml_to_csv():
    # Parse the XML file
    tree = ET.parse('data/PrixCarburants_annuel_2022.xml')
    root = tree.getroot()

    # Initialize lists to store data
    locations = []
    gas_types = []
    dates = []
    prices = []
    code_postals = []

    # Iterate through the pdv elements in the XML
    for pdv in root.findall('pdv'):
        location_id = pdv.get('id')
        code_postal = pdv.get('cp')
        for prix in pdv.findall('prix'):
            gas_type = prix.get('nom')
            date = prix.get('maj')
            price = prix.get('valeur')

            # Append data to lists
            locations.append(location_id)
            code_postals.append(code_postal)
            gas_types.append(gas_type)
            dates.append(date)
            prices.append(price)

    # Create a DataFrame
    data = {
        'Location_ID': locations,
        'Code_Postal': code_postals,
        'Gas_Type': gas_types,
        'Date': dates,
        'Price': prices
    }

    df = pd.DataFrame(data)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.date


    # Print the DataFrame
    #print(df)

    df.to_csv('data/PrixCarburants_annuel_2022.csv', index=False)