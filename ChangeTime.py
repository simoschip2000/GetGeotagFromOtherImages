import sys
from pyexiv2 import Image as ImgMeta
import dateutil.parser
from datetime import timedelta

#https://stackoverflow.com/questions/53543549/change-exif-data-on-jpeg-without-altering-picture

DTO_KEY = 'Exif.Photo.DateTimeOriginal'
filename = sys.argv[1]
offset_hours = int(sys.argv[2])


with ImgMeta(filename) as img_meta:

    exif = img_meta.read_exif()
    try:
        dto = exif[DTO_KEY]
    except KeyError:
        raise
    
    
    #https://stackoverflow.com/questions/9507648/datetime-from-string-in-python-best-guessing-string-format
    img_date = dateutil.parser.parse(dto)
    
    img_date = img_date + timedelta(hours=offset_hours)
    
    img_date_string = img_date.strftime("%Y:%m:%d %H:%M:%S")
   
    img_meta.modify_exif({DTO_KEY: img_date_string})