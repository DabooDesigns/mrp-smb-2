from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    for fl in self.file_loader_1.files:
      fl1 = self.Image_Resizer_change(fl)
      unique_id = self.item['id']
      app_tables.product_images.add_row(image=fl1, product_id=unique_id)
#      print (unique_id)
  
    open_form('Admin_Product_View')

  def Image_Resizer_change(self, file, **event_args):
    filename = file.name
#    tfile = anvil.image.generate_thumbnail(file, 120) 
    mfile = anvil.image.generate_thumbnail(file, 480) 
    lfile = anvil.image.generate_thumbnail(file, 1200) 

    tstrings = ["thumbnail", filename]
    tfilename = "-".join(tstrings)
    mstrings = ["m", filename]
    mfilename = "-".join(mstrings)    
    lstrings = ["l", filename]
    lfilename = "-".join(lstrings)    

    image_medium = anvil.server.call("name_image",mfile,mfilename)
    anvil.media.download(image_medium)  
    image_large = anvil.server.call("name_image",lfile,lfilename)    
    return image_large
  
