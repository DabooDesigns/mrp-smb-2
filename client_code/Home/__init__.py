from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
#    self.email_label.text = user['email']  

#    role_info = anvil.server.call("get_my_role")  
#    self.role_label.text = role_info

#    role_info = anvil.server.call("get_my_company")  
#    self.customer_company_label.text = role_info

#    role_info = anvil.server.call("get_my_info")  

#    my_email = (role_info[0])
#    my_role = (role_info[1])
#    my_company = (role_info[2])

#    self.email_label.text = my_email
#    self.role_label.text = my_role
#    self.customer_company_label.text = my_company

#    product_number = anvil.server.call("get_next_product_number")
#    print(product_number)