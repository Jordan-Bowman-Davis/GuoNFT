import PIL.Image
from PIL import ImageFont, ImageDraw, Image

# character and size specifications
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
new_width = 100
new_height = None

def resize(image):
    global new_height
    old_width, old_height = image.size
    new_height = (int)((new_width * old_height) * 0.5 // old_width)
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

def main(fileName):
    # import image
    path = "/Users/jordanbowman-davis/Documents/Code Projects/GuoNFT/images/" + fileName
    print(path)
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")

    print("image uploaded")
    
    # process image & convert to ASCII string
    image = resize(image)
    print("image re-sized")
    greyscale_image = to_greyscale(image)
    print("image to greyscale")
    ascii_str = pixel_to_ascii(greyscale_image)
    print("image to ascii")
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""

    # split string based on image width
    print("starting split")
    newlinect = 0
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
        newlinect = newlinect + 1

    ascii_img = ascii_img + (" " * (new_width - 26)) + "made by jkb3@princeton.edu"

    # save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
        #f.write((" " * (new_width - 26)) + "made by jkb3@princeton.edu")

    # text file back to png image
    print(new_width, new_height)
    img = Image.new('RGB', (7 * new_width, 15 * new_height + 12), color = (255,255,255))
    fnt = ImageFont.truetype("/Users/jordanbowman-davis/Documents/Code Projects/GuoNFT/Menlo-Regular.ttf", 11)
    ImageDraw.Draw(img).text((0,0), ascii_img, font=fnt, fill=(0,0,0))
    img.save("/Users/jordanbowman-davis/Documents/result.png")