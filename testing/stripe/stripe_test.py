#goal -> create a customer

import stripe
from config import STRIPE_KEY

stripe.api_key = STRIPE_KEY
#stripe.Customer.create(description="My First Test Customer")
print(stripe.Customer.list(limit=3))
stripe.Customer.delete("cus_") 
