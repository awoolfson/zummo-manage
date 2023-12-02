from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from get_records import get_records
from get_services import extract_number_from_recordid, extract_tech_from_recordid
from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SERVICES
from pyairtable import Api
from datetime import datetime
from edit_method import edit_db, add_to_db
from generate_new_id import get_id_from_service_id
import pytz

app = Flask(__name__)
CORS(app)

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
    # fields = request.args.get('fields')
    fields = request.get_json()
    record_info = get_records(services_tbl, fields)

    #Getting information related to links to other airtables
    link_to_phone = record_info[0]["fields"].get("Phone Number", None)
    if link_to_phone is not None:
        link_to_phone = link_to_phone[0]
        record_info[0]["fields"]["Phone Number"][0] = extract_number_from_recordid(link_to_phone)
    else:
        # Handle the case where the 'Phone Number' field is missing
        # Set to a default value or handle accordingly
        record_info[0]["fields"]["Phone Number"] = None
    
    link_to_tech = record_info[0]["fields"].get("Assigned Tech", None)
    if link_to_tech is not None:
        link_to_tech = link_to_tech[0]
        record_info[0]["fields"]["Assigned Tech"][0] = extract_tech_from_recordid(link_to_tech)
    else:
        # Handle the case where the 'Assigned Tech' field is missing
        # Set to a default value or handle accordingly
        record_info[0]["fields"]["Assigned Tech"] = None
    
    #Converting ISO 8601 formatted dates into a more readable form
    iso_string = record_info[0]["fields"].get("Drop-off date", None)
    print(iso_string)
    if iso_string is not None:
        dt_object_utc = datetime.fromisoformat(iso_string[:-1]).replace(tzinfo=pytz.UTC)
        local_tz = pytz.timezone('America/New_York')
        dt_object_local = dt_object_utc.astimezone(local_tz)
        formatted_date = dt_object_local.strftime('%-m/%-d/%Y %-I:%M%p')
        print(formatted_date)
        record_info[0]["fields"]["Drop-off date"] = formatted_date
    else:
        # Handle the case where the 'Drop-off date' field is missing
        # Set to a default value or handle accordingly
        record_info[0]["fields"]["Drop-off date"] = None
    return record_info

@app.route("/add-to-db", methods=["POST"])
def add_to_table():
    data = request.json
    print(data)
    # Extract data from the request and add it to the Airtable using the modified add_to_db method
    record_id = add_to_db("Service Requested", data["Service Requested"], AIRTABLE_TEST_SERVICES)
    edit_db(record_id, "Bike Description", data["bikeInformation"], AIRTABLE_TEST_SERVICES)
    edit_db(record_id, "Customer Comments", data["customerComments"], AIRTABLE_TEST_SERVICES)
    edit_db(record_id, "Technician Comments", data["technicianComments"], AIRTABLE_TEST_SERVICES)
    edit_db(record_id, "Service Status", data["serviceStatus"], AIRTABLE_TEST_SERVICES)
    return jsonify({"success": True}), 200
    
@app.route("/edit-db", methods=["POST"])
def edit_table():
    #print(request.get_json())
    data = request.get_json()
    #print(data[0]["fields"]["Service Bike ID"])
    #print(data[0]["id"])
    print(data[0]["fields"]["Requested Completion Date"])
    #print(get_id_from_service_id(data[0]["fields"]["Service Bike ID"]))

    edit_db(data[0]["id"], "Bike Description", data[0]["fields"]["Bike Description"], AIRTABLE_TEST_SERVICES)
    edit_db(data[0]["id"], "Customer Comments", data[0]["fields"]["Customer Comments"], AIRTABLE_TEST_SERVICES)
    edit_db(data[0]["id"], "Technician Comments", data[0]["fields"]["Technician Comments"], AIRTABLE_TEST_SERVICES)
    edit_db(data[0]["id"], "Service Requested", data[0]["fields"]["Service Requested"], AIRTABLE_TEST_SERVICES)
    edit_db(data[0]["id"], "Service Performed", data[0]["fields"]["Service Performed"], AIRTABLE_TEST_SERVICES)
    edit_db(data[0]["id"], "Service Status", data[0]["fields"]["Service Status"], AIRTABLE_TEST_SERVICES)
    #edit_db(data[0]["id"], "Requested Completion Date", data[0]["fields"]["Requested Completion Date"], AIRTABLE_TEST_SERVICES)
    return jsonify({"success": True}), 200
    
if __name__ == "__main__":
    app.run(debug=True)
    