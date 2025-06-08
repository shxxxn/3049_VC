from PIL import Image

def vc_decrypt(path1, path2):
    s1 = Image.open(path1).convert("1")
    s2 = Image.open(path2).convert("1")
    width, height = s1.size
    result = Image.new("1", (width, height))

    for x in range(width):
        for y in range(height):
            result.putpixel((x, y), s1.getpixel((x, y)) & s2.getpixel((x, y)))

    result_path = "recovered.png"
    result.save(result_path)
    return result_path
