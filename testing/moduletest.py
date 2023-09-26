# Airtable API/.env test 
import os
from dotenv import load_dotenv
from flask import Flask, render_template
import requests as rq

load_dotenv() 
AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_TEST_BASE_ID = (os.getenv("AIRTABLE_BASEID")) #-> str: #initalizes base ID
AIRTABLE_TEST_CONTACTS = (os.getenv("AIRTABLE_CONTACTS")) #-> str: #initalizes table

app = Flask(__name__)

@app.route('/')
def index():
    # Make a GET request to the Airtable API with the personal access token
    url = f'https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_CONTACTS}'
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}

    airtable_response = rq.get(url, headers=headers)
    if airtable_response.status_code == 200:
        data = airtable_response.json()
        records = data.get('records', [])
        return render_template('index.html', records=records)
    else:
        return f'Error: {airtable_response.status_code} - {airtable_response.text}'

if __name__ == '__main__':
    app.run(debug=True)
