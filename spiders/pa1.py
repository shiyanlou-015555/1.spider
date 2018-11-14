import tesserocr
from PIL import Image
image = Image.open('timg.jpeg')
image.show()
print(tesserocr.image_to_text(image))

