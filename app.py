import os
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask


def generate_qr(link, filename):
    folder = "qr-image"
    if not os.path.exists(folder):
        os.makedirs(folder)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=25,
        border=2,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(radius_ratio=1),
        eye_drawer=RoundedModuleDrawer(radius_ratio=1),
        color_mask=SolidFillColorMask(
            front_color=(200, 150, 101), back_color=(32, 29, 30)
        ),
    )

    file_path = os.path.join("qr-image", filename)
    img.save(file_path)
    print(f"Success! Saved to: {file_path}")


if __name__ == "__main__":
    my_link = input("Paste the URL you want to encode: ")
    generate_qr(my_link, "al-ald-qr.png")
