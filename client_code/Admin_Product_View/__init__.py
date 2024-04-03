from ._anvil_designer import Admin_Product_ViewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Admin_Product_Edit import Admin_Product_Edit


class Admin_Product_View(Admin_Product_ViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_products()

    # Any code you write here will run before the form opens.
  def refresh_products(self):
    self.products_panel.items = anvil.server.call('get_products')

#  def build_sku_prefix():
#  def get_short(string, howmany):
#    nosp = string.replace(" ", "")
#    short = nosp[:howmany]
#    return short    
  
  def button_1_click(self, **event_args):
    new_product = {}

    # Open an alert displaying the 'EntryEdit' Form
    save_clicked = alert(
      content=Admin_Product_Edit(item=new_product),
      title="Add Product",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
#      short2 = self.get_short('stuff1' '5')
#      print (short2)
      customer_company_short = anvil.server.call('get_short', 'customer_company', 5)
      sku = {customer_company_short}
      anvil.server.call('add_products', new_product)
      
      self.refresh_products()
    pass
