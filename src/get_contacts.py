from pyairtable import Table
import re
from config import AIRTABLE_PAT, AIRTABLE_BASE_ID, AIRTABLE_CONTACTS

def get_contact_by_phone(phone_number: str) -> list:
    contacts_tbl = Table(AIRTABLE_PAT, AIRTABLE_BASE_ID, AIRTABLE_CONTACTS)
    contacts = contacts_tbl.all()
    
    phone_number = re.sub(r'[^0-9]', '', phone_number)
    
    matches = []
    
    for contact in contacts:
        if other := contact.get('fields', {}).get('Phone Number'):
            other = re.sub(r'[^0-9]', '', other)
            if other == phone_number:
                matches.append(contact)
    
    return matches