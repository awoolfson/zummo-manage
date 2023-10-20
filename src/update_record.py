from pyairtable import Api, Table
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES
from get_records import get_records
from pprint import pprint

# UNTESTED
def update_record(id: str, fields: dict, table: Table) -> list:
    return table.update(id, fields, replace=True)
    
def main():
    if __name__ == "__main__":
        # tests on service table bike id 18 currently
        api = Api(AIRTABLE_PAT)
        services_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES)
        pprint(services_tbl.all())
        # get user input for ID
        id = 'recv3WWFenwUY2JZV'
        fields = {"Bike Description": None}
        print(update_record(id, fields, services_tbl))
        
main()