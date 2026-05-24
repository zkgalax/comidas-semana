import qrcode

# 1. El enlace de tu página web de comidas
url = "https://zkgalax.github.io/comidas-semana/"

# 2. Creamos el objeto QR con la configuración básica
qr = qrcode.make(url)

# 3. Guardamos la imagen en la misma carpeta donde tienes el script
qr.save("Python/qr_menu_semanal.png")

print("¡Código QR generado con éxito como 'qr_menu_semanal.png'!")