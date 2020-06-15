from PIL import Image


def convert_bmp_to_png(file_name, transparent_rgb):
    file_name = str(file_name)

    image: Image = Image.open(file_name)
    image = image.convert("RGBA")

    img_data = image.getdata()
    new_data = list()

    for item in img_data:
        if item[0] == transparent_rgb[0] and item[1] == transparent_rgb[1] and item[2] == transparent_rgb[2]:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append((item[0], item[1], item[2], 255))

    image.putdata(new_data)
    image.save(file_name.replace(".bmp", ".png"), "PNG")
