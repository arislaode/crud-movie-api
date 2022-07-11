import os
from dotenv import load_dotenv
import base64

load_dotenv()

filename = 'rrr.jpg'

image = os.path.join(os.getenv("UPLOAD_FOLDER"), filename)

print(base64.b64encode(image))