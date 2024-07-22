import barcode

# ean13
a = barcode.get_barcode_class('ean13')
value = a('1234567890123') # Only contain Number which can't exceed 13 character
s =value.save('1')

#  Code 39
from barcode.writer import ImageWriter

a = barcode.get_barcode_class('code39')
value = a('Founder and board Vice Chairman ', writer=ImageWriter())
s =value.save('a1')