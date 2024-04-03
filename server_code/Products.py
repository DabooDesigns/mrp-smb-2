import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import autoinc

@anvil.server.callable
def get_short(string, howmany = 5):
  nosp = string.replace(" ", "")
  short = nosp[:howmany]
  return short.upper()
  
@anvil.server.callable
def get_products():
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  return app_tables.products.search(
    tables.order_by("created", ascending=False)
  )

@anvil.server.callable
def add_products(product_dict):
  print (product_dict)
  print (product_dict['customer_company']['name'])
  ccval = (product_dict['customer_company']['name'])
  print (ccval)
  id = anvil.server.call('get_next_product_number')


  ccvalret = anvil.server.call('get_short', ccval)
  strings = [ccvalret, str(id)]
  joined_string = "-".join(strings)
  print(joined_string)  # Output: apple-banana-cherry
#  print (ccvalret)  
  app_tables.products.add_row(
    id=id,
    sku=joined_string,
    #   id=anvil.server.call('get_next_product_number'),
    created=datetime.now(),

    **product_dict
  )

@anvil.server.callable
def update_products(product, product_dict):
  # check that the entry given is really a row in the ‘entries’ table
  if app_tables.products.has_row(entry):
    product_dict['updated'] = datetime.now()
    product.update(**product_dict)
  else:
    raise Exception("Product does not exist")

@anvil.server.callable
def delete_products(product):
  # check that the entry being deleted exists in the Data Table
  if app_tables.products.has_row(product):
    product.delete()
  else:
    raise Exception("Product does not exist")

@anvil.server.callable
def add_product_images(product_image_dict)
  print (product_image_dict)
  print (product_image_dict['image']['image'])
  app_tables.product_images.add_row(
  created=datetime.now(),

    
    **product_dict
  )