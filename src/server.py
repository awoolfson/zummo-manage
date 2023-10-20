from flask import Flask, send_from_directory, request
from get_records import get_records
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES
from pyairtable import Api

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/get-services-by-id", methods = ['POST'])
def get_services():
    api = Api(AIRTABLE_PAT)
    services_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES)
    fields = request.args.get('fields')
    return get_records(services_tbl, fields)
    
if __name__ == "__main__":
    app.run(debug=True)
    