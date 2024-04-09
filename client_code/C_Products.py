import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def say_hello():
  print("Hello, world")



# May need to create another variable as a way to send the user back to a page when the file load operation has been completed.
#    open_form('Form1')

# Resizes the uploaded image(s) resizes to 480w and initiates a download and stores a 1200w in the product_images table
def Image_Resizer_change(self, file, **event_args):
  filename = file.name
#   tfile = anvil.image.generate_thumbnail(file, 120) 
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