from pyairtable import Api
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES

def get_services_by_id(id: str) -> list:
    api = Api(AIRTABLE_PAT)
    services_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES)
    services = services_tbl.all()
    
    matches = []
    
    for service in services:
        if other := service.get('fields', {}).get('Service Bike ID'):
            if other == id:
                matches.append(service)
    
    return matches

def main():
    if __name__ == "__main__":
        # get user input for ID
        id = int(input("Enter a service id: "))
        print(get_services_by_id(id))
        
main()