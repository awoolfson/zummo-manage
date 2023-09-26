from dotenv import load_dotenv
import os

load_dotenv()

AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_TEST_BASE_ID = "appr8SepSgx9SP6ir"
AIRTABLE_TEST_CONTACTS = "tblXBR1YTXYvGhwWJ"
