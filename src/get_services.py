from pyairtable import Api
import re
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES

def get_services_by_phone(phone_number: str) -> list:
    api = Api(AIRTABLE_PAT)
    services_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES)
    services = services_tbl.all()
    
    print(services)
    
    phone_number = re.sub(r'[^0-9]', '', phone_number)
    
    matches = []
    
    for service in services:
        if other := service.get('fields', {}).get('Phone Number'):
            other = re.sub(r'[^0-9]', '', other)
            if other == phone_number:
                matches.append(service)
    
    return matches

def main():
    if __name__ == "__main__":
        # get user input for phone number
        phone_number = input("Enter a phone number: ")
        print(get_services_by_phone(phone_number))
        
main()