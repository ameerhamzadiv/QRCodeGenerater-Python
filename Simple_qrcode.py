import qrcode as qr
from datetime import datetime

#QRcode image name
inputName = input("Enter your qrcode name: ")

#qrcode link or text for generate
input = input("Enter link or text for generate qrcode: ")

# get current datetime
current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

#merge qrcode image name and current datetime
setname = f'{inputName}-{current_time}'

#generate qrcode
genqr = qr.make(input)

#save qrcode with unique name
saveqr = genqr.save(f'{setname}.png')

print('QR Code generate check your files directory')



