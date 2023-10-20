### this is the initial testing space for the edit methods 

from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_TABLE
from pyairtable import Api
import re
import requests as rq
from pprint import pprint
#not using flask just yet

#inital vars
api = Api(AIRTABLE_PAT) #personal access token
test_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_TABLE) #info about test table
full_tbl = test_tbl.all()

def add_to_db(usr_field: str, usr_update: str):
    usr_edit = {usr_field: usr_update}
    test_tbl.create(usr_edit)

def delete_from_db(item_id: str):
    usr_delete = {"id": item_id}
    test_tbl.delete(item_id)

def get_fields(): 
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_TABLE}'
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
    response = rq.get(url, headers=headers)
    data = response.json()
    fields = data['records'][0]['fields'].keys() #records -> index 0 -> fields, return list of keys
    return fields

def main():
    if __name__ == "__main__":
        answer = input("What do you want to do - Add an item (a) or Delete an item (d): ")
        if answer == "a":
            # asks user for field name and what they would to add to it
            fields = get_fields()
            print(f"These are the field names {fields}")
            fieldname = input("Enter field name as they appear in the string here: ")
            newitem = input("Enter what you would like to add to the field here: ")
            add_to_db(fieldname, newitem)
        elif answer == "d":
            print(f"This is a refrence you can use to find the id of the item you would like to delete")
            pprint(full_tbl)
            item_id = input("What is the id of the item you would like to delete: ")
            delete_from_db(item_id)
        else:
            main()
main()