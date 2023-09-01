import qrcode

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(filename)

website_url = "https://web.znorm.org/"
qr_code_filename = "website_qrcode.png"

generate_qr_code(website_url, qr_code_filename)
print(f"QR code for {website_url} generated and saved as {qr_code_filename}")
