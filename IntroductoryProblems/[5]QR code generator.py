#importing qrcode library
import qrcode
#Entering link from user
link=input("enter link")
#converting that link into qr
qr=qrcode.make(link)
#saving qr as image (optional)
qr_img=qr.save("qrcode.png")
#showing qr code
qr.show()