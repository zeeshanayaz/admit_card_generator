from PIL import Image, ImageDraw, ImageFont


def _font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold
        else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


def create_gender_placeholders(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    specs = [
        ("male_placeholder.png", "MALE", "M"),
        ("female_placeholder.png", "FEMALE", "F"),
    ]

    for filename, label, initial in specs:
        path = output_dir / filename
        if path.exists():
            continue

        img = Image.new("RGB", (500, 580), "white")
        draw = ImageDraw.Draw(img)

        # Simple neutral silhouette placeholder.
        cx = 250
        draw.ellipse((175, 70, 325, 220), fill=(170, 170, 170), outline=(80, 80, 80), width=4)
        draw.rounded_rectangle(
            (105, 220, 395, 500),
            radius=80,
            fill=(180, 180, 180),
            outline=(80, 80, 80),
            width=4,
        )

        title_font = _font(38, True)
        small_font = _font(30, True)

        bbox = draw.textbbox((0, 0), label, font=title_font)
        draw.text(
            ((500 - (bbox[2] - bbox[0])) / 2, 515),
            label,
            fill=(50, 50, 50),
            font=title_font,
        )

        img.save(path)


if __name__ == "__main__":
    create_gender_placeholders(__import__("pathlib").Path("assets"))
