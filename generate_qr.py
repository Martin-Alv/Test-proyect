# generate_qr.py
import qrcode

# Datos para generar el código QR
data = "https://tu-enlace-aqui.com"

# Crear la instancia del QR
qr = qrcode.QRCode(
    version=1,  # Tamaño del código QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada caja (pixel) en el QR
    border=4,  # Tamaño del borde alrededor del QR
)

# Añadir datos
qr.add_data(data)
qr.make(fit=True)

# Crear la imagen del QR
img = qr.make_image(fill="black", back_color="white")

# Guardar la imagen en un archivo
img.save("qr_code.png")

print("Código QR generado y guardado como 'qr_code.png'")
