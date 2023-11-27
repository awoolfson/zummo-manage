from pypdf import PdfWriter, PdfReader
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pyairtable import Api

from get_records import get_records
from get_services import get_services_by_id

from config import AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_EMPLOYEES_AND_VOLUNTEERS, AIRTABLE_TEST_SALES_ORDERS, AIRTABLE_TEST_CONTACTS

info = {
    "issued_to": None,
    "description": None,
    "total": None,
    "date": datetime.now(),
    "invoice_number": None,
}

def get_service_info(service_id: str, info: dict):
    service = get_services_by_id(service_id)
    if fields := service[0].get("fields"):
        api = Api(AIRTABLE_PAT)
        table = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_EMPLOYEES_AND_VOLUNTEERS)
        info["issued_to"] = fields.get("Customer Name", "N/A")
        
        info["description"] = """
        drop off date: {0}
        bike: {1}
        requested completion date: {2}
        assigned technician: {3}
        technician comments: {4}
        """.format(
            fields.get("Drop-off date", "N/A"),
            fields.get("Bike Description", "N/A"),
            fields.get("Requested completion date", "N/A"),
            table.get(fields.get("Assigned Tech")[0])["fields"].get("Name", "N/A"),
            fields.get("Technician Comments", "N/A")
            )
        
        info["total"] = fields.get("Total", "N/A")
    
def get_sales_info(order_num: str, info: dict):
    api = Api(AIRTABLE_PAT)
    sales_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SALES_ORDERS)
    order = get_records(sales_tbl, {"Order Number": order_num})
    if fields := order[0].get("fields"):
        
        contacts_tbl = api.table(AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_CONTACTS)
        contact_fields = contacts_tbl.get(fields.get("Customer", "N/A"))["fields"]
        info["issued_to"] = contact_fields.get("First Name", "") + " " + contact_fields.get("Last Name", "")
        
        if date := fields.get("Invoice Date"):
            info["date"] = date
            
        info["description"] = ""
        
        info["total"] = fields.get("Total Order Value", "N/A")
        

def generate_invoice(invoice_number: str, info: dict, is_service: bool, id: str):
    template = Image.open("../invoices/zummo-invoice-template.png")
    invoice = ImageDraw.Draw(template)
    
    info["invoice_number"] = invoice_number
    
    if is_service:
        get_service_info(id, info)
        print(info)
    else:
        get_sales_info(id, info)
        
    font = ImageFont.truetype("../invoices/fonts/JetBrainsMonoNL-Regular.ttf", 22) 
    invoice.text((490, 330), info["invoice_number"], fill=(0, 0, 0), font=font)
    invoice.text((490, 450), str(info["date"]), fill=(0, 0, 0), font=font)
    invoice.text((490, 575), info["issued_to"], fill=(0, 0, 0), font=font)
    description = info["description"].split("\n")
    for i in range(len(description)):
        invoice.text((400, 690 + (i * 20)), description[i], fill=(0, 0, 0), font=font)
    invoice.text((680, 1322), info["total"], fill=(0, 0, 0), font=font)
    
    template.show()
    
generate_invoice("1", info, True, "3")
generate_invoice("1", info, False, "5")
