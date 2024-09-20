from django.db import models

# Create your models here.
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/', blank=True)
    qr_code_image = models.ImageField(upload_to='qr_codes/', blank=True, editable=False)

    def save(self, *args, **kwargs):
        # Generate QR code if background image is provided
        if self.background_image:
            # URL to encode in QR code
            qr_url = f"http://192.168.1.78:8000{self.background_image.url}"

            # Create QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=2,
            )
            qr.add_data(qr_url)
            qr.make(fit=True)

            # Create QR code image
            qr_img = qr.make_image(fill='black', back_color='white').convert("RGBA")

            # Open the background image
            background = Image.open(self.background_image)

            # Resize the QR code
            qr_size = (80, 80)
            qr_img = qr_img.resize(qr_size)

            # Determine position for QR code
            position = (background.width - qr_size[0] - 10, 10)  # Top-right corner

            # Paste QR code onto the background image
            background.paste(qr_img, position, qr_img)

            # Save combined image
            buffer = BytesIO()
            background.save(buffer, format="PNG")
            self.qr_code_image.save(f'qr_{self.pk}.png', File(buffer), save=False)

        super().save(*args, **kwargs)
