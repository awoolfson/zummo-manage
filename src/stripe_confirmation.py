#intention - Ability to flag the bikes as sold after the payment has been successfully processed/Ability to store Stripe payment confirmation in the Airtable 'Sales order' table
import stripe
from config import STRIPE_KEY, AIRTABLE_PAT, AIRTABLE_TEST_BASE_ID, AIRTABLE_TEST_SALES_ORDERS 
from edit_method import edit_db
import requests as rq

stripe.api_key = STRIPE_KEY

def stripe_payment_confirmation(amountpayed: int, usr_currency: str, order_number: int): #creates a payment intent, sends bike sold message to airtable sales order table
    id = get_id_from_ordernum(order_number)
    edit_db(id, "Status", AIRTABLE_TEST_SALES_ORDERS, "Invoiced") #store stripe payment confirmation in airtable
    return stripe.PaymentIntent.create(amount=amountpayed, currency=usr_currency) #currency is the positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00) from: https://stripe.com/docs/api/payment_intents/create?lang=python 

def get_id_from_ordernum(order_number): #find our id from our ordernumber
    url = f"https://api.airtable.com/v0/{AIRTABLE_TEST_BASE_ID}/{AIRTABLE_TEST_SALES_ORDERS}"
    headers = {'Authorization': f'Bearer {AIRTABLE_PAT}'}
    response = rq.get(url, headers=headers)
    if response.status_code == 200: #if we get a response
        data = response.json().get('records', []) #give us a json of whats inside records
        for record in data:
            fields = record.get('fields', {})
            if fields.get('Order Number') == order_number:
                return record['id']  # Return the id of the matching record
    else:
        return f"error {response.status_code}" #return error code if there is an error


def main():
        if __name__ == "__main__":
            print(get_id_from_ordernum(1)) #it works, yayyyy!
            print(stripe_payment_confirmation(2000,"usd", 1)) #2000 cents = 20 dollars
main()