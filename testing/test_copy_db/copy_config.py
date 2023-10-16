#config for a copy of test db, just to make sure nothing gets messed up, 
#for your PAT to work for files in test_copy_db, your PAT needs access to
#the copy of the database called MY COPY OF Zummo Bike Shop Test DB 
#which was posted in the google spaces chat

#also this table wont accept attachments because it is on the free version

from dotenv import load_dotenv
import os

load_dotenv()

AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token

# for airtable test instance

############### str: -> initalizes tables
AIRTABLE_TEST_BASE_ID = "appR0IZli0H5rk36M" 
AIRTABLE_TEST_CONTACTS = "tblntHMUjH8rfMtK4"
AIRTABLE_TEST_EMPLOYEES_AND_VOLUNTEERS = "tblKVGYZSu55ikKhS"
AIRTABLE_TEST_SERVICES = "tbls9wOBwvvOvyyas"
AIRTABLE_TEST_BIKES_FOR_SALE = "tblmseLpDyOBmxOYV"
AIRTABLE_TEST_BIKES_FOR_DONO = "tbl6dESp3pEMPyOyT"
AIRTABLE_TEST_RENTAL_BIKES = "tblLvbJDF9HrvN2L2"
AIRTABE_TEST_WEBSHOP_INQUIRY = "tblAC7qsvHg846KBK"
AIRTABLE_TEST_SALES_ORDERS = "tblPTUb3tFSJdsDAm"
AIRTABLE_TEST_ORDER_ITEMS = "tbl2CelZZotbUblzA"
AIRTABLE_TEST_INTERACTIONS = "tblovBMXnQZq4QkyV"
AIRTABLE_TEST_NO_LONGER_USER_SALES = "tblDDDslxSvOaf7lk"
AIRTABLE_TEST_RENTAL = "tbl0L8tqy71omEGGh" 
AIRTABLE_COPY_TEST_TABLE = "tbl9VsmARUiM5Mm3k" #this table only exists in the copy db