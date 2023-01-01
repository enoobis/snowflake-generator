import os
import random
from PIL import Image, ImageFilter , ImageDraw

for i in range(6000):
    img = Image.new('RGBA' , (500,500), 'black')
    idraw = ImageDraw.Draw(img)

    for x in range(0,9):
        for y in range(0,9):
            rand = random.randint(0,1)
            if rand == 0:
                idraw.rectangle((x*50,y*50,(x*50)+50,(y*50)+50),fill = "white")
              
    # flip the image in each direction
    img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img4 = img3.transpose(Image.FLIP_LEFT_RIGHT)

    # create a new image to paste the four versions into
    result = Image.new('RGB', (1000,1000))

    result.paste(img, (0, 0))
    result.paste(img2, (500, 0))
    result.paste(img3, (0, 500))
    result.paste(img4, (500, 500))
  
    # save the result
    resultfull = Image.new('RGB', (1100,1100),"black")
    resultfull.paste(result,(50,50))
    new_path = os.path.join('images', '' + str(i) + '.jpg')
    resultfull.save(new_path)

