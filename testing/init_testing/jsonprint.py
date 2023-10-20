# Airtable json print test - taken out of test_get because this is still used for testing
import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, render_template
import requests as rq
from pprint import pprint #used to pretty print response.json

#inital vars
load_dotenv() 
AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_TEST_BASE_ID = "appr8SepSgx9SP6ir" #-> str: # initalizes test base id


AIRTABLE_TABLE = input("Copy and paste the id of the table you want to print: ") #-> str: #initalizes table
url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TABLE}'
headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
response = rq.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    records = data.get('records', [])
pprint(data)