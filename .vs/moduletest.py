##Airtable API/.env test 
import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, render_template
import requests as rq


load_dotenv() 
PAT = (os.getenv("PAT")) #-> str: #initalizes personal access token
BASE = "appr8SepSgx9SP6ir" #zummobikes base id
TBL = "tblXBR1YTXYvGhwWJ" #zummobikes table id
app = Flask(__name__)

@app.route('/')
def index():
    # Make a GET request to the Airtable API with the personal access token
    url = f'https://api.airtable.com/v0/{BASE}/{TBL}'
    headers = {'Authorization': f'Bearer {PAT}'}

    response = rq.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        records = data.get('records', [])
        return render_template('index.html', records=records)
    else:
        return f'Error: {response.status_code} - {response.text}'

if __name__ == '__main__':
    app.run(debug=True)

