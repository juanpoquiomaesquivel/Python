# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/juanp/Escritorio/Python/miniproyectos/myqrcode.png")

result = decode(img)

print(result)

"""
import qrcode

data = 'Don\'t forget to susccribe'

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='white')
img.save('C:/Users/juanp/Escritorio/Python/miniproyectos/myqrcode1.png')
"""