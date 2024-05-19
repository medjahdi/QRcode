import qrcode
link= eval(input("What do you want to put inside the qrcode? "))
qr = qrcode.make(f"{link}")
qr.show(qr)
print("Your QRCode was succesful generated !")