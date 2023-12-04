#used to generate new service bike id's manually
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES 
import requests as rq

def generate_new_service_id():
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_SERVICES}'
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}

    response = rq.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        records = data.get('records', [])
        service_array = [record['fields'].get("Service Bike ID", 0) for record in records] #get an array of the service id's
        if service_array: #if service array exists
            return max(service_array) + 1 #return the new id, which was the previous greatest id plus 1
    print(f"Error: {response.status_code}") #you got this error
    return 0 #return id of 0 if we didin't get any id's 

def get_id_from_service_id(service_id: int):
    url = f"https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_SERVICES}"
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
    response = rq.get(url, headers=headers)
    if response.status_code == 200: #if we get a response
        data = response.json().get('records', []) #give us a json of whats inside records
        for record in data:
            fields = record.get('fields', {})
            if fields.get('Service Bike ID') == service_id:
                return record['id']  # Return the id of the matching record
    else:
        return f"error {response.status_code}" #return error code if there is an error

def main():
        if __name__ == "__main__":
            print(f"Our new id is {generate_new_service_id()}") #prints out our new id
            print(f"The id of the row with service bike id 1 is {get_id_from_service_id(1)}")
main()