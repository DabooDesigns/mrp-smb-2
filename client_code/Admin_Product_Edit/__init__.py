from ._anvil_designer import Admin_Product_EditTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Admin_Product_Edit(Admin_Product_EditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#    self.categories = [(cat['name'], cat) for cat in app_tables.categories.search()]
#    self.category_box.items = self.categories
    self.user_companies = [(uc['name'], uc) for uc in app_tables.user_company.search()]
    self.customer_company.items = self.user_companies
    self.product_category = [(uc['category'], uc) for uc in app_tables.product_category.search()]
    self.category.items = self.product_category


    
    self.manufacturing_instructions.toolbar = anvil.server.call('quill_toolbar')
# Any code you write here will run before the form opens.

