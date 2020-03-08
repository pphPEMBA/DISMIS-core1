from PIL import Image
import pytesseract
import os


imagepath = 'Screenshot from 2020-03-06 11-13-35.png'


img = Image.open(imagepath)
text = pytesseract.image_to_string(img)
os.system('clear')
print(text)