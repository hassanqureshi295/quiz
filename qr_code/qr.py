import qrcode as qr
from PIL import Image
# Simple QR code
# user = input("Enter the link: ")
# img = qr.make(user)
# img.save("Greeting.png")

# Customization

code = qr.QRCode(version=1,
error_correction=qr.constants.ERROR_CORRECT_H,
box_size=10, border=4)

code.add_data("Hello Wassup!")
code.make(fit=True)
img = code.make_image(fill_color="blue", back_color="white")
img.save("new_qr.png")
