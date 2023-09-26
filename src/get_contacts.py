from pyairtable import Api
import re
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_CONTACTS

def get_contact_by_phone(phone_number: str) -> list:
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

if __name__ == "__main__":
    print("Insert contact number here: ")
    contactnumber = input() #-> str:
    print(get_contact_by_phone(contactnumber)) #insert phone number, prints out all users information contained within contacts