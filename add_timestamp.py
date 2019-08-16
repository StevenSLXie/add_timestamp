# -*- coding: utf-8 -*-


from PIL import Image, ExifTags,ImageFont, ImageDraw
import os
import math
import sys

exit_set = []

#path = '/Users/StevenSLXie/Documents/Python_projects/ide_experiment'

def main(path):

    dest = os.path.join(path,'processed')
    if not os.path.exists(dest):
        os.mkdir(dest)
        
    for roots, dirs, files in os.walk(path):
        for file_ in files:
            ext = os.path.splitext(file_)[-1].lower()
            if ext == '.jpeg' or ext == '.jpg' or ext == '.png':
                img = Image.open(os.path.join(roots, file_))
                if img._getexif() is not None:
                    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items()}
                    time_tag = 'DateTimeOriginal' 
                    if time_tag in exif:
                        draw = ImageDraw.Draw(img)
                        font = ImageFont.truetype('/Library/Fonts/Arial.ttf',math.floor(0.03*img.size[0]))
                        date_time = exif[time_tag][0:4] + '-' + exif[time_tag][5:7] + '-' + exif[time_tag][8:10]  
                        draw.text((0.8*img.size[0], 0.93*img.size[1]),date_time,(255,255,255),font=font)
                        img.save(os.path.join(roots,'processed/'+file_))
                        exit_set.append(exif['DateTimeOriginal' ])

if __name__ == '__main__':
    main(sys.argv[1])
