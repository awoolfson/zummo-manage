### this is the initial testing space for the edit methods

from copy_config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_COPY_TEST_TABLE
from pyairtable import Api
import re


#inital vars
api = Api(AIRTABLE_PAT) #personal access token
test_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_COPY_TEST_TABLE) #info about test table
full_tbl = test_tbl.all() #equal to data.json(), everything in the test table

def edit_db(usr_request: str):
    