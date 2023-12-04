from dotenv import load_dotenv
import os

load_dotenv()

AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token

# for airtable test instance

############### str: -> initalizes tables
AIRTABLE_TEST_BASE_ID = "appr8SepSgx9SP6ir" 
AIRTABLE_TEST_CONTACTS = "tblXBR1YTXYvGhwWJ"
AIRTABLE_TEST_EMPLOYEES_AND_VOLUNTEERS = "tblk3Qd3sKV9JPNtx"
AIRTABLE_TEST_SERVICES = "tbl2hG3F6LlSW3Bm7"
AIRTABLE_TEST_BIKES_FOR_SALE = "tblWAo0tdOEFN2RaA"
AIRTABLE_TEST_BIKES_FOR_DONO = "tblGlO7tDFuQg3RKy"
AIRTABLE_TEST_RENTAL_BIKES = "tbllDlYHfpxvWi5XH"
AIRTABE_TEST_WEBSHOP_INQUIRY = "tblaKhFw5X6cvBNNp"
AIRTABLE_TEST_SALES_ORDERS = "tblp14q73VINEXGM1"
AIRTABLE_TEST_ORDER_ITEMS = "tblCKoA3zEjflGoLf"
AIRTABLE_TEST_INTERACTIONS = "tblYDL11X6PuvlnKA"
AIRTABLE_TEST_NO_LONGER_USER_SALES = "tbldLNHp78lSBKaxZ"
AIRTABLE_TEST_RENTAL = "tblATiIu8nRsN9JSW" 
AIRTABLE_TEST_TABLE = "tblLBiaTHqXPozzOs" #this table only exists for testing
AIRTABLE_STRIPE_TESTS = "tblB0tyxKfjkLbbW8" #this table exists for testing stripe integration

#for stripe integration

STRIPE_KEY = (os.getenv("STRIPE_KEY")) #-> str: #initalizes api key - stripe
