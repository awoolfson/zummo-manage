from pyairtable import Api
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES
from get_records import get_records
from pprint import pprint

def get_services_by_id(id: str) -> list:
    api = Api(AIRTABLE_PAT)
    services_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES)
    return get_records(services_tbl, {'Service Bike ID': id})


def main():
    if __name__ == "__main__":
        # get user input for ID
        id = int(input("Enter a service id: "))
        pprint(get_services_by_id(id))
        
main()