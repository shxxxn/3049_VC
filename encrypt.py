from PIL import Image
import random

def vc_encrypt(image_path):
    img = Image.open(image_path).convert("1")
    width, height = img.size

    share1 = Image.new("1", (width * 2, height * 2))
    share2 = Image.new("1", (width * 2, height * 2))

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            pattern = random.choice([0, 1])
            if pixel == 0:
                p1, p2 = ([1, 0], [0, 1]) if pattern else ([0, 1], [1, 0])
            else:
                p1, p2 = ([1, 0], [1, 0]) if pattern else ([0, 1], [0, 1])

            for dx in range(2):
                for dy in range(2):
                    share1.putpixel((x * 2 + dx, y * 2 + dy), p1[dy])
                    share2.putpixel((x * 2 + dx, y * 2 + dy), p2[dy])

    share1_path = "share1.png"
    share2_path = "share2.png"
    share1.save(share1_path)
    share2.save(share2_path)
    return share1_path, share2_path
