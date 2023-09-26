from dotenv import load_dotenv
import os

load_dotenv()

AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_BASEID = (os.getenv("AIRTABLE_BASEID")) #-> str: #initalizes base ID
AIRTABLE_CONTACTS = (os.getenv("AIRTABLE_CONTACTS")) #-> str: #initalizes contacts table
AIRTABLE_EMPLOYEESandVOLUNTEERS = (os.getenv("AIRTABLE_EMPLOYEESandVOLUNTEERS")) #-> str: #initalizes employees and volunteers table
AIRTABLE_SERVICE = (os.getenv("AIRTABLE_SERVICE")) #-> str: #initalizes service table
AIRTABLE_BIKESforSALE = (os.getenv("AIRTABLE_BIKESforSALE")) #-> str: #initalizes initializes bikes for sale table
AIRTABLE_BIKESforDONO = (os.getenv("AIRTABLE_BIKESforDONO")) #-> str: #initalizes bikes for donation table
AIRTABLE_RENTALBIKES = (os.getenv("AIRTABLE_RENTALBIKES")) #-> str: #initalizes rental bikes table
AIRTABE_WEBSHOPINQUIRY = (os.getenv("AIRTABE_WEBSHOPINQUIRY")) #-> str: #initalizes web shop inquiry table
AIRTABLE_SALESORDERS = (os.getenv("AIRTABLE_SALESORDERS")) #-> str: #initalizes sales orders table
AIRTABLE_ORDERITEMS = (os.getenv("AIRTABLE_ORDERITEMS")) #-> str: #initalizes order items table
AIRTABLE_INTERACTIONS = (os.getenv("AIRTABLE_INTERACTIONS")) #-> str: #initalizes interactions table
AIRTABLE_NOLONGERUSERSALES = (os.getenv("AIRTABLE_NOLONGERUSERSALES")) #-> str: #initalizes no longer user sales table
AIRTABLE_RENTAL = (os.getenv("AIRTABLE_RENTAL")) #-> str: #initalizes rental table