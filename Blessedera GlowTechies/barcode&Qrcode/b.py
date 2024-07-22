import qrcode
from PIL import pillow

b = qrcode.make("Son of God")
b.save('./img/test.png') 

bc = qrcode.QRCode(
    version = 1,
    box_size =15,
    border = 1
)

website =  'https://adeife.pythonanywhere.com/'
bc.add_data(website)
bc.make(fit=True)
img = bc.make_image(fill_color='gold', back_color='blue')
img.save('./img/web-qrcode2.png')