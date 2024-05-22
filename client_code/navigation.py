import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from Admin_Customer_Orders import Admin_Customer_Orders
from Admin_Home import Admin_Home
from .Admin_Product_Edit import Admin_Product_Edit
from .Admin_Product_View import Admin_Product_View

home_form = None

def get_form():
  if not home_form:
    raise Exception("You must set the home form first.")
  return home_form

def go_home():
  set_active_nav('home')
  set_title("")
  form = get_form()
  user = anvil.users.get_user()
  if user:
    form.load_component(HomeDetailsComponent())
  else:
    form.load_component(HomeAnonComponent())