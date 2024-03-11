# to do https://www.wikidata.org/wiki/Property:P625 add lat long!

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
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
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
        coord = result['coord']['value']
        print("City:", city_name)
        print("Population:", population)
        print("Coordinates:", coord)
else:
    print("Failed to retrieve data. Status code:", response.status_code)