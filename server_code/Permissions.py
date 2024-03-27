import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_my_role():
  user = anvil.users.get_user()
  if user == None:
    return

  if user != None:
    my_role = (user['user_role']['user_role_list'])
#    print (my_role)
    
    return my_role

@anvil.server.callable
def get_my_company():
  user = anvil.users.get_user()
  if user == None:
    return
  if user != None:
    my_company = (user['customer_company']['name'])
    return my_company

@anvil.server.callable
def get_my_info():
  user = anvil.users.get_user()
  if user == None:
    return
  if user != None:
    my_email = (user['email'])
    my_role = (user['user_role']['user_role_list'])   
    my_company = (user['customer_company']['name'])
    return my_email, my_role, my_company


