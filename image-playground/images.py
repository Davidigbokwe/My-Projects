from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
img.thumbnail((400,266))
img.save('thumbnail.jpg')


print(img.size)