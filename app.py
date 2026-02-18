import qrcode


def generate_qr(link, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="darkblue", back_color="white")

    img.save(filename)
    print(f"Success! Saved as {filename}")


if __name__ == "__main__":
    my_link = input("Paste the URL you want to encode: ")
    generate_qr(my_link, "ceramic-qr.png")
