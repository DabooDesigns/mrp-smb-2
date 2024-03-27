import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from PIL import Image
import io

def name_image(file, name):
  img = Image.open(io.BytesIO(file.get_bytes()))
  bs = io.BytesIO()
  img.save(bs, format="JPEG")
  return anvil.BlobMedia("image/jpeg", bs.getvalue(), name=name)

@anvil.server.callable
def quill_toolbar():
    toolbar_options = [
    ['bold', 'italic', 'underline', 'strike'],  # Toggled buttons
    ['blockquote', 'code-block'],  # Block-level formatting
#    [{'header': 1}, {'header': 2}],  # Custom button values for headers
    [{'list': 'ordered'}, {'list': 'bullet'}, {'list': 'check'}],  # Lists
#    [{'script': 'sub'}, {'script': 'super'}],  # Superscript/subscript
    [{'indent': '-1'}, {'indent': '+1'}],  # Indentation
#    [{'direction': 'rtl'}],  # Text direction
#    [{'size': ['small', False, 'large', 'huge']}],  # Custom dropdown for font size
    [{'header': [1, 2, 3, 4, 5, 6, False]}],  # Header styles
    [{'color': []}, {'background': []}],  # Dropdowns for text color and background
#    [{'font': []}],  # Font selection
    [{'align': []}],  # Text alignment
    ['link'],
    ['image'], # Image 
    ['clean']  # Remove formatting button
    ]
    return toolbar_options