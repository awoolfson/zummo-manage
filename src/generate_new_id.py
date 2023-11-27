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

def main():
        if __name__ == "__main__":
            print(f"Our new id is {generate_new_service_id()}") #prints out our new id

main()