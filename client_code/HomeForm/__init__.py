from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Home import Home
from ..Admin_Home import Admin_Home
from ..Admin_Product_View import Admin_Product_View
from ..Admin_Customer_Orders import Admin_Customer_Orders
from ..navigation import navigation

class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role_router()

  
  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.sign_in.text = email
    else:
      self.sign_in.text = "Sign In"
  
  def sign_in_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
      logout = confirm("Would you like to logout?")
      if logout:
        anvil.users.logout()
        self.role_router()        
    else:
      anvil.users.login_with_form()
      self.change_sign_in_text()
      self.role_router()        
  
  def go_to_admin(self):
    self.content_panel.clear()
    self.content_panel.add_component(Admin_Home())
    self.item['admin_menu_visible'] = True
    self.refresh_data_bindings()
  
  def go_to_supervisor(self):
    print("Supervisor")
    
  def go_to_team_member(self):
    print("Team Member")
    
  def go_to_customer(self):
    print("Customer")  

  def go_to_signed_out(self):
    self.content_panel.clear()
    self.content_panel.add_component(Home())
    self.item['admin_menu_visible'] = False
    self.refresh_data_bindings()
  
  def role_router(self):
    self.change_sign_in_text()
    user_role = anvil.server.call("get_my_role")
    self.item['admin_menu_visible'] = False
    self.item['customer_menu_visible'] = False    
    self.refresh_data_bindings()
    if user_role == 'Admin':
      self.go_to_admin()
    elif user_role == 'Supervisor':
      self.go_to_supervisor()
    elif user_role == 'Team Member':
      self.go_to_team_member()
    elif user_role == 'Customer':
      self.go_to_customer()
    else:
      self.go_to_signed_out()


  def link_admin_products_click(self, **event_args):
#    self.link_admin_products.role='selected'
    self.content_panel.clear()
    self.content_panel.add_component(Admin_Product_View())
#    self.refresh_data_bindings()
    pass

  def link_Home_click(self, **event_args):
# #    self.link_Home.role='selected'
#     self.content_panel.clear()
#     self.content_panel.add_component(Home())
#     pass
    navigation.go_home()

  def link_admin_customer_orders_click(self, **event_args):
#    self.link_admin_products.role='selected'
    self.content_panel.clear()
    self.content_panel.add_component(Admin_Customer_Orders())
    pass

