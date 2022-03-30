import requests

listings = 'category'
listings_endpoint = f'http://localhost:8000/auction/api/{listings}?name=gun'

listing_response = requests.get(listings_endpoint)
print(listing_response.json())

