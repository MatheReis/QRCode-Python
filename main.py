import qrcode

qr = qrcode.QRCode(
    version= 1,
    error_correction = qrcode.ERROR_CORRECT_L,
    box_size = 30,
    border = 2,
)


image = qrcode.make('https://modalgr.com.br/')
image.save('qrcode-modalgr.png')
