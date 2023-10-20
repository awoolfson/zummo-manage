from pyairtable import Api
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES
from get_records import get_records

# UNTESTED
def update_services(id: str, fields: dict) -> list:
    api = Api(AIRTABLE_PAT)
    services_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES)
    return services_tbl.update(id, fields)
    