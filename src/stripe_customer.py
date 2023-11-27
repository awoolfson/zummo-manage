#initial customer methods

import stripe
from config import STRIPE_KEY

stripe.api_key = STRIPE_KEY

def create_customer(usr_description: str = None, email_adr: str = None, phone_num: str = None, cus_address: dict = None):  #create customer, description, email, phone number, and address field are optional
    return stripe.Customer.create(description=usr_description, email = email_adr, phone = phone_num, address = cus_address) #returns customer object created

def retrieve_customer(cus_id: str): #retrives customer of a given id, found in the "id" field 
    return stripe.Customer.retrieve(cus_id) #returns customer object


def update_customer(cus_id: str, field: str, data = None, metafield: str = None): #updates a customer of a given id, updates the field entered with the data entered
#possible fields to update: "address", "balance", "description",  "email" and everything else listed here: https://stripe.com/docs/api/customers/update
#metadata is a unique field that can be added with this function - metadata takes a dictonary as an argument, so metafield is an optional parameter that names the field of the dictonary
#be careful with the data arguement because data can include multiple datatypes, be sure to use the api refrence linked above

    if field == "metadata":
        return stripe.Customer.modify(cus_id,metadata={metafield:data}) #returns customer object modified, now with "metadata" field
    elif field == "address":
        return stripe.Customer.modify(cus_id, address=data) #returns customer object modified
    else:
        return stripe.Customer.modify(cus_id, **{field:data}) #returns customer object modified
        #note, if we end up needing to this function can be greatly expanded with more parameters: https://stripe.com/docs/api/customers/update

def list_customers(list_limit: int = None, email_adr = None): #lists customers with optional list limit parameter and with the option of searching by customer email
                                                            
    if list_limit != None:
        return stripe.Customer.list(limit = list_limit) #return the amount of customers in the list_limit arguement
    elif email_adr != None:
        return stripe.Customer.list(email = email_adr) #return the customers with the email in the cus_email argument
    else:
        return stripe.Customer.list() #return a list of 10 customers
    #note, if we end up needing to this function can be greatly expanded with more parameters: https://stripe.com/docs/api/customers/list

def delete_customer(cus_id: str): #deletes a customer of a given id
    return stripe.Customer.delete(cus_id) #returns an object with a deleted parameter on success.

def search_customers(search_query: str): #search query must follow parameters given here https://stripe.com/docs/search#search-query-language
    return stripe.Customer.search(query=search_query)
    #note, if we end up needing to this function can be greatly expanded with more parameters: https://stripe.com/docs/api/customers/search

def main():
    if __name__ == "__main__":
        #address = {'line1': 'Scary town', 'city': 'evil city', 'state': 'OHIO', 'postal_code': '10000', 'country': 'US'}
        #print(create_customer(email_adr="bob@steven.com", cus_address=address))
        #print(retrieve_customer("cus_P0DzJ9mCuo4fTo")) #this is only going to work for me, insert the customer id you generate to test this
        #print(list_customers(list_limit=1))
        #print(list_customers(list_limit=1, email_adr="bob@steven.com"))
        #print(list_customers(email_adr="bob@steven.com"))
        #update_customer(cus_id="cus_P0DzJ9mCuo4fTo", field = "metadata", data = "hi", metafield = "hi")
        #print(retrieve_customer("cus_P0DzJ9mCuo4fTo"))
        #update_customer(cus_id="cus_P0DzJ9mCuo4fTo", field = "address", data = address)
        #print(retrieve_customer("cus_P0DzJ9mCuo4fTo"))
        #update_customer(cus_id="cus_P0DzJ9mCuo4fTo", field = "email", data = "steven@bob.com")
        #print(retrieve_customer("cus_P0DzJ9mCuo4fTo"))
        #print(delete_customer("cus_P0EMjC7qn8kDda"))
        #print(search_customers("email:'steven@bob.com'"))
        return

##Still editing liines
intent = stripe.PaymentIntent.create(
    amount=1000,  # Amount in cents
    currency='usd',
    payment_method_types=['card']
)

# Print the client secret for the PaymentIntent (for client-side implementation)
print(intent.client_secret)

main()
