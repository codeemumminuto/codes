#pip install qrcode
import qrcode
image = qrcode.make("https://www.tiktok.com")
imagem.save("myqrcode.jpg")