import qrcode
from PIL import Image
import qrcode.constants
logolink = './img/logo.png'
logo = Image.open(logolink)


basewidth = 100

width =(basewidth/float(logo.size[0]))
hsize = int(float(logo.size[1]) *float(width))
logow = logo.resize((basewidth, hsize )) #, Image.ANTIALIAS
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

website =  'https://adeife.pythonanywhere.com/'
QRcode.add_data(website)
QRcode.make()

img = QRcode.make_image(fill_color='gold', back_color='white') #.convert('RGB')

pos = ((img.size[0] - logow.size[0])//2,
        (img.size[1] - logow.size[1]) //2 )
img.paste(logow, pos)

img.save('./img/web-qrcodewithImage2.png')
print('QRCODE Generated')