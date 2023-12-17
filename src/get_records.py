from pyairtable import Table
from pyairtable.formulas import match

def get_records(table: Table, fields: dict) -> list:
    formula = match(fields)
    try:
        matches = table.all(formula=formula)
    except:
        matches = []
        print('Error: Invalid field(s) or value(s)')
    return matches
