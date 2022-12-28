# projects
import pyqrcode
import png
from pyqrcode import *

url = input("ENTER URL HERE : ")
save_as = input("Enter filename for save as : ")

qrcode = pyqrcode.create(url)
print("QRcode succesfull created")

url.svg(save_as,scale=8)

url.png(save_as,scale=6)

# www.linkedin.com/in/abhishakejutur
# https://www.instagram.com/abhishakejutur/

cv2.destroyAllWindows()
