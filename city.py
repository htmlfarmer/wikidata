from wikidata.client import Client

import requests

# Define the SPARQL query
sparql_query = """
SELECT ?city ?cityLabel ?population ?coord
WHERE {
  ?city wdt:P31/wdt:P279* wd:Q515.
  ?city wdt:P625 ?coord.
  ?city wdt:P1082 ?population.
  SERVICE wikibase:around {
    ?city wdt:P625 ?cityCoord.
    bd:serviceParam wikibase:center "Point(-43.1729 -22.9068)"^^geo:wktLiteral.
    bd:serviceParam wikibase:radius "500".
  }
  SERVICE wikibase:label { bd:service# Define the SPARQL query
"""

# Define the Wikidata SPARQL endpoint URL
endpoint_url = "https://query.wikidata.org/sparql"

# Define the request headers
headers = {
    'User-Agent': 'Example/1.0',
    'Accept': 'application/sparql-results+json'
}

# Define the request parameters
params = {
    'query': sparql_query,
    'format': 'json'
}

# Send the HTTP GET request
response = requests.get(endpoint_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON response
    data = response.json()

    # Extract coordinates from the response
    for item in data['results']['bindings']:
        coord = item['coord']['value']
        latitude, longitude = map(float, coord.split(' ')[1:])
        print("Latitude:", latitude)
        print("Longitude:", longitude)
else:
    print("Failed to retrieve data. Status code:", response.status_code)Param wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

# Define the endpoint URL for Wikidata's SPARQL query service
endpoint_url = "https://query.wikidata.org/sparql"

# Define the request headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Define the request parameters
params = {
    'format': 'json',
    'query': sparql_query
}

# Execute the SPARQL query
response = requests.get(endpoint_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON response
    data = response.json()

    # Print the results
    for result in data['results']['bindings']:
        city_name = result['cityLabel']['value']
        population = result['population']['value']
        print("City:", city_name)
        print("Population:", population)
else:
    print("Failed to retrieve data. Status code:", response.status_code)

# Define the SPARQL query
sparql_query = """
SELECT ?city ?cityLabel ?coord
WHERE {
  ?city rdfs:label "Rio de Janeiro"@en.  # Replace "Rio de Janeiro" with the city name you're interested in
  ?city wdt:P625 ?coord.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

# Define the Wikidata SPARQL endpoint URL
endpoint_url = "https://query.wikidata.org/sparql"

# Define the request headers
headers = {
    'User-Agent': 'Example/1.0',
    'Accept': 'application/sparql-results+json'
}

# Define the request parameters
params = {
    'query': sparql_query,
    'format': 'json'
}

# Send the HTTP GET request
response = requests.get(endpoint_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON response
    data = response.json()

    # Extract coordinates from the response
    for item in data['results']['bindings']:
        coord = item['coord']['value']
        latitude, longitude = map(float, coord.split(' ')[1:])
        print("Latitude:", latitude)
        print("Longitude:", longitude)
else:
    print("Failed to retrieve data. Status code:", response.status_code)

from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Earth radius in kilometers

    return distance

# Example coordinates for Rio de Janeiro
rio_lat = -22.9068
rio_lon = -43.1729

# Example coordinates for another city
city_lat = # Latitude of the other city
city_lon = # Longitude of the other city

distance = haversine(rio_lat, rio_lon, city_lat, city_lon)
print("Distance between Rio de Janeiro and the other city:", distance, "kilometers")