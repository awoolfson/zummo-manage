import os
from dotenv import load_dotenv
from flask import Flask, render_template
from pyairtable import Table

load_dotenv()

AIRTABLE_PAT = (os.getenv("AIRTABLE_PAT")) #-> str: #initalizes personal access token
AIRTABLE_TEST_BASE_ID = "appr8SepSgx9SP6ir" #initalizes base id
AIRTABLE_TEST_CONTACTS = "tblXBR1YTXYvGhwWJ" #initalizes contacts table

app = Flask(__name__)

@app.route('/')
def index():    
    tbl = Table(AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_CONTACTS)
    contacts = tbl.all()
    return render_template('index.html', records=contacts)

if __name__ == '__main__':
    app.run(debug=True)
