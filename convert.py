import csv
import json

pub_fields = [
    # IDs
    'id', 
    'pubNumber', 
    # Name and summary
    'name', 
    'summary',  
    # Address
    'address1', 
    'city', 
    'county', 
    'postcode',
    # Region
    'region',
    'subRegion',
    # Coordinates 
    'lng', 
    'lat', 
    # Contact
    'telephone',
    # Metadata
    'isHotel', 
    'isAirport',
]


def extract_pubs(raw_spoons_data):
    for region in raw_spoons_data:
        for subregion in region['subRegions']:
            for raw_pub in subregion['items']:
                pub = {field: raw_pub.get(field) for field in pub_fields}
                pub['region'] = region['region']
                pub['subRegion'] = subregion['name']
                yield pub


if __name__ == '__main__':
    with open('spoons.json') as f:
        raw_spoons_data = json.load(f)

    with open('spoons.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=pub_fields)
        writer.writeheader()
        for pub in extract_pubs(raw_spoons_data):
            writer.writerow(pub)


            
            
