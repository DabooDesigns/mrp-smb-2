from ._anvil_designer import Admin_Product_EditTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from ..validation import Validator
from form_checker import validation


class Admin_Product_Edit(Admin_Product_EditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#    self.categories = [(cat['name'], cat) for cat in app_tables.categories.search()]
#    self.category_box.items = self.categories
    user = anvil.users.get_user()
    user_company = user['customer_company']['name']
#    print (user_company)
    self.user_companies = [(uc['name'], uc) for uc in app_tables.user_company.search()]
    self.customer_company.items = self.user_companies

    self.product_status = [(uc['status'], uc) for uc in app_tables.product_status.search()]
    self.status.items = self.product_status
    
    self.manufacturing_instructions.toolbar = anvil.server.call('quill_toolbar')

    self.validator = validation.Validator()
#    self.validator.require(self.customer_company, self.validate_company)

    self.validator.require(self.customer_company, ['change'],
                           self.customer_company.selected_value is not None,
                           self.validate_company)  
#    self.validator.require(self.name, self.validate_name)
#    self.validator.require(self.category, self.validate_category)
    
    # Uncomment the line below to disable the button until the form is complete:
    #self.validator.enable_when_valid(self.submit_btn)
  
  # Any code you write here will run before the form opens.

#    anvil.media.download(image_medium)

  def customer_company_change(self, **event_args):
    self.product_category = [(uc['category'], uc) for uc in app_tables.product_category.search(customer_company=self.item['customer_company'])]
    self.category.items = self.product_category


 






