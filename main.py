from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 100)
FONT_COLOR = "#06043B"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    name_width = draw.textlength(name, font=FONT_FILE)
    name_height=0

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2+20), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":

    with open("names.txt", "r") as f:
        lines = f.readlines()
    names=[]
    # Iterate over the lines and add each line as a list to the new list
    for line in lines:
        names.append(line.strip())
    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")

