from dotenv import load_dotenv
import os

load_dotenv()

AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_TEST_BASE_ID = (os.getenv("AIRTABLE_TEST_BASE_ID")) #-> str: #initalizes base ID
AIRTABLE_TEST_CONTACTS = (os.getenv("AIRTABLE_TEST_CONTACTS")) #-> str: #initalizes table