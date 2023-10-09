from flask import Flask, send_from_directory, request
from get_records import get_records

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/get-services")
def get_services():
    name = request.args.get('name')
    phone_number = request.args.get('phone_number')
    

if __name__ == "__main__":
    app.run(debug=True)