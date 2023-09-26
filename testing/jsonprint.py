# Airtable json print test
import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, render_template
import requests as rq
from pprint import pprint #used to pretty print response.json

load_dotenv() 
AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_BASE_ID = "appr8SepSgx9SP6ir" #initalizes base id
AIRTABLE_CONTACTS = "tblXBR1YTXYvGhwWJ" #initalizes contacts table
url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_CONTACTS}'
headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
response = rq.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    records = data.get('records', [])
pprint(data)