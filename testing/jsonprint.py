# Airtable json print test
import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, render_template
import requests as rq
from pprint import pprint #used to pretty print response.json

load_dotenv() 
AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_BASEID = (os.getenv("AIRTABLE_BASEID")) #-> str: #zummobikes base id
AIRTABLE_CONTACTS = (os.getenv("AIRTABLE_CONTACTS")) #-> str: #zummobikes table id
url = f'https://api.airtable.com/v0/{AIRTABLE_BASEID}/{AIRTABLE_CONTACTS}'
headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
response = rq.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    records = data.get('records', [])
pprint(data)