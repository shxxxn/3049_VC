import qrcode
import cv2
from pyzbar.pyzbar import decode

def generate_qrcode(text):
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qr_path = "qrcode.png"
    img.save(qr_path)
    return qr_path

def scan_qrcode(image_path):
    img = cv2.imread(image_path)
    decoded_objs = decode(img)
    return decoded_objs[0].data.decode('utf-8') if decoded_objs else None
