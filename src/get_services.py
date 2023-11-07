from pyairtable import Api
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES
import requests as rq
from pprint import pprint

def get_services_by_id(id: str) -> list:
    api = Api(AIRTABLE_PAT)
    services_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES)
    services = services_tbl.all()
    
    matches = []
    response = "" #string put in matches
    #id <- input (service id of bike)
    #response = name/phone number

    for service in services:
        if other := service.get('fields', {}).get('Service Bike ID'):
            if other == id:
                response += (f"The name of the person working on this is {service.get('fields', {}).get('First Name (from Phone Number)')}, ")
                recordid = service.get('fields', {}).get('Phone Number')[0] #get the id for the record that has the phone number, it will be a one member list so index 0 converts it to string
                response += (f"the phone number of the person working on this is {extract_number_from_recordid(recordid)}.")
                matches.append(response)
    return matches

def extract_number_from_recordid(recordid):
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_SERVICES}/{recordid}'
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
    response = rq.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        number = data['fields']['Phone Number'] #the targetted record -> phone number -> return corresponding key
        return number
    else:
        return "not found"

def extract_info_from_record(recordid): #use this if you want everything stored in a particular record, ex: all the info stored in the phone number section
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_SERVICES}/{recordid}' 
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
    response = rq.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    if __name__ == "__main__":
        # get user input for ID
        id = int(input("Enter a service id: "))
        print(get_services_by_id(id))
        
main()