from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID
from pyairtable import Api
import re
import requests as rq
from pprint import pprint
import json
#not using flask just yet

#inital vars - pyairtable
api = Api(AIRTABLE_PAT) #personal access token

def add_to_db(usr_field: str, usr_update: str, AIRTABLE_TABLE: str): #add a completely column to table, does not work on specific fields
    test_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TABLE) #info about table 
    full_tbl = test_tbl.all()
    usr_edit = {usr_field: usr_update}
    test_tbl.create(usr_edit)

def edit_db(item_id: str, usr_field: dict, usr_update: str, AIRTABLE_TABLE: str): #edits an entry in an existing field
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TABLE}'
    updated_records = {"records": [{"id": item_id,
     "fields": {usr_field: usr_update}}]}
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}','Content-Type': 'application/json'}
    data = json.dumps(updated_records)
    response = rq.request("PATCH", url, headers=headers, data=data)

def clear_id(item_id: str, AIRTABLE_TABLE: str): #deletes every entry of a certain id
    test_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TABLE) #info about table
    full_tbl = test_tbl.all()
    test_tbl.delete(item_id)

def delete_item(item_id: str, usr_field: dict, AIRTABLE_TABLE: str): #replaces a single entry
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TABLE}'
    updated_records = {"records": [{"id": item_id,
     "fields": {usr_field: None}}]}
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}','Content-Type': 'application/json'}
    data = json.dumps(updated_records)
    response = rq.request("PATCH", url, headers=headers, data=data)

def get_fields(AIRTABLE_TABLE: str): 
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TABLE}'
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
    response = rq.get(url, headers=headers)
    data = response.json()
    fields = data['records'][0]['fields'].keys() #records -> index 0 -> fields, return list of keys
    return fields

def main():
    if __name__ == "__main__":
        table = input("Which table do you want to edit (enter table id): ")
        url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{table}' #testing to see if this response works
        headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
        response = rq.get(url, headers=headers)
        if response.status_code != 200:
            print("Table does not exist.")
            main()
        answer = input("What do you want to do - Add an item (a), Delete an item (d), Update an entry in a table (u), or exit the function (e): ")
        if answer == "e":
            return
        elif answer == "a":
            # asks user for field name and what they would to add to it
            fields = get_fields(table)
            print(f"These are the field names {fields}")
            fieldname = input("Enter field name as they appear in the list here: ")
            newitem = input("Enter what you would like to add to the field here: ")
            add_to_db(fieldname, newitem, table)
            return
        elif answer == "d":
            answer2 = input("Would you like to delete every item of a single id (1), or a single entry of a single id (2)?")
            if answer2 == "1":
                print(f"This is a refrence you can use to find the id and field of the item you would like to delete")
                test_tbl = api.table(AIRTABLE_TEST_BASE_ID, table) #info about table 
                full_tbl = test_tbl.all()
                pprint(full_tbl)
                item_id = input("What is the id you would like to clear?: ")
                clear_id(item_id, table)
                return
            elif answer2 == "2":    
                print(f"This is a refrence you can use to find the id and field of the item you would like to delete")
                test_tbl = api.table(AIRTABLE_TEST_BASE_ID, table) #info about table 
                full_tbl = test_tbl.all()
                pprint(full_tbl)
                item_id = input("What is the id of the item you would like to delete: ")
                fieldname = input("What is the field of the item you would like to delete: ") #going to replace the item corresponding with this id/field combination w/null
                delete_item(item_id, fieldname, table)
                return
            else:
                print("Please answer 1 or 2.")
                main()
        elif answer == "u":
            print(f"This is a refrence you can use to find the id and field of the item you would like to update")
            test_tbl = api.table(AIRTABLE_TEST_BASE_ID, table) #info about table
            full_tbl = test_tbl.all()
            pprint(full_tbl)
            item_id = input("What is the id of the item you would like to edit: ")
            fieldname = input("What is the field of the item you would like to edit: ") #going to replace the item corresponding with this id/field combination w/the user input
            usr_update = input("What is the text you want to insert into this area: ")
            edit_db(item_id, fieldname, usr_update, table) 
        else:
            print("Please answer a, d, e or u.")
            main()
main()
