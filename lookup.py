# to do https://www.wikidata.org/wiki/Property:P625 add lat long!

import requests

def get_lat_lon(city_name):
    # Define the base URL for the Nominatim API
    base_url = "https://nominatim.openstreetmap.org/search"

    # Define the parameters for the API request
    params = {
        'q': city_name,
        'format': 'json'
    }

    # Send the HTTP GET request to the Nominatim API
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if any results were returned
        if data:
            # Extract latitude and longitude from the first result
            lat = float(data[0]['lat'])
            lon = float(data[0]['lon'])
            
            return lat, lon
        else:
            print("No results found for the city:", city_name)
            return None, None
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None, None

# Example usage:
city_name = input("Enter the name of the city: ")
latitude, longitude = get_lat_lon(city_name)

if latitude is not None and longitude is not None:
    print("Latitude:", latitude)
    print("Longitude:", longitude)