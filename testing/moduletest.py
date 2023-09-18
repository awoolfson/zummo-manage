# Airtable API/.env test 
import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, render_template
import requests as rq


load_dotenv() 
AIR_PAT = (os.getenv("AIR_PAT")) #-> str: #initalizes personal access token
AIR_BASE = "appr8SepSgx9SP6ir" #-> str: #zummobikes base id
AIR_TBL = "tblXBR1YTXYvGhwWJ" #-> str: #zummobikes table id
app = Flask(__name__)

@app.route('/')
def index():
    # Make a GET request to the Airtable API with the personal access token
    url = f'https://api.airtable.com/v0/{AIR_BASE}/{AIR_TBL}'
    headers = {'Authorization': f'Bearer {AIR_PAT}'}

    response = rq.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        records = data.get('records', [])
        return render_template('index.html', records=records)
    else:
        return f'Error: {response.status_code} - {response.text}'

if __name__ == '__main__':
    app.run(debug=True)

