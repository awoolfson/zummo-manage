from pyairtable import Api
import re
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_EMPLOYEES_AND_VOLUNTEERS

def get_employees_by_name(mechanic_name: str) -> list:
    api = Api(AIRTABLE_PAT)
    employees_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_EMPLOYEES_AND_VOLUNTEERS)
    employees = employees_tbl.all()

    mechanic_name = mechanic_name.lower()

    matches = []

    for employee in employees:
        if name := employee.get('fields', {}).get('Name'):
            if mechanic_name in name.lower():
                matches.append(employee)

    return matches