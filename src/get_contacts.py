from pyairtable import Api
import re
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_CONTACTS

def get_contacts_by_phone(phone_number: str) -> list:
    api = Api(AIRTABLE_PAT)
    contacts_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_CONTACTS)
    contacts = contacts_tbl.all()
    
    phone_number = re.sub(r'[^0-9]', '', phone_number)
    
    matches = []
    
    for contact in contacts:
        if other := contact.get('fields', {}).get('Phone Number'):
            other = re.sub(r'[^0-9]', '', other)
            if other == phone_number:
                matches.append(contact)
    
    return matches

def main():
    if __name__ == "__main__":
        # get user input for phone number
        phone_number = input("Enter a phone number: ")
        print(get_contacts_by_phone(phone_number))
        
main()