#John Asaro :3 -> im proud of this one im signing it 

#Story 23 - Bike management - Ability to search bikes by key fields (size, bike type, etc.)  in the Airtable 'Bikes for sale' table

from pyairtable import Api
import re
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_BIKES_FOR_SALE
import requests as rq

#inital vars
api = Api(AIRTABLE_PAT) #personal acess token
bike_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_BIKES_FOR_SALE) #info about test table, in the bikes for sale branch
bikes = bike_tbl.all() #equal to data.json(), everything in the bikes for sale table

def get_bikes_by_field(bike_field: str) -> list:
    matches = [] #list that is received 
    fields = get_fields()
    for field in fields:
        result = [bike.get('fields', {}).get('Model name/Number') for bike in bikes if bike['fields'].get(field) == bike_field] #get the name of the bike if the keyword is contained within a field in fields
        matches.extend(result)
    return matches

def get_fields(): #it is IMPOSSIBLE to do this using pyairtable... probably, I tried for a long time
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_BIKES_FOR_SALE}'
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
    response = rq.get(url, headers=headers)
    data = response.json()
    fields = data['records'][0]['fields'].keys() #records -> index 0 -> fields, return list of keys
    return fields


def main():
    if __name__ == "__main__":
        # asks user for keyword
        bike_field = input("Search for bike by keyword: ")
        print(get_bikes_by_field(bike_field))

main()
