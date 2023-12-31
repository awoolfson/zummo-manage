### this is the initial testing space for the edit methods 

from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_TABLE
from pyairtable import Api
import re
import requests as rq
from pprint import pprint
import json
#not using flask just yet

#inital vars - pyairtable
api = Api(AIRTABLE_PAT) #personal access token
test_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_TABLE) #info about test table
full_tbl = test_tbl.all()

#initial vars - airtable api
url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_TABLE}'

def add_to_db(usr_field: str, usr_update: str):
    usr_edit = {usr_field: usr_update}
    test_tbl.create(usr_edit)

def clear_id(item_id: str): #deletes every entry of a certain id
    test_tbl.delete(item_id)

def delete_item(item_id: str, usr_field: dict): #replaces a single entry
    updated_records = {"records": [{"id": item_id,
     "fields": {usr_field: None}}]}
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}','Content-Type': 'application/json'}
    data = json.dumps(updated_records)
    response = rq.request("PATCH", url, headers=headers, data=data)

def get_fields(): 
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
            fieldname = input("Enter field name as they appear in the list here: ")
            newitem = input("Enter what you would like to add to the field here: ")
            add_to_db(fieldname, newitem)
        elif answer == "d":
            answer2 = input("Would you like to delete every item of a single id (1), or a single entry of a single id (2)?")
            if answer2 == "1":
                print(f"This is a refrence you can use to find the id and field of the item you would like to delete")
                pprint(full_tbl)
                item_id = input("What is the id you would like to clear?: ")
                clear_id(item_id)
            elif answer2 == "2":    
                print(f"This is a refrence you can use to find the id and field of the item you would like to delete")
                pprint(full_tbl)
                item_id = input("What is the id of the item you would like to delete: ")
                fieldname = input("What is the field of the item you would like to delete: ") #going to replace the item corresponding with this id/field combination w/null
                delete_item(item_id, fieldname)
            else:
                main()
        else:
            main()
main()