import datetime
import os
import secrets
from PIL import Image, ImageOps
from src import app

def get_datetime():
    '''
    Return list [date, time]
    '''
    date_now = datetime.datetime.now().strftime("%Y/%m/%d")
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    return [date_now, time_now]


def save_profile_picture(form_picture):
    '''
    Input: Picture picture image file from user form
    - Convert input picture to 200x200
    - Save it with random hex(8) name
    
    Return: Saved image name
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    output_size = (200, 200)
    i = Image.open(form_picture)
    i = ImageOps.exif_transpose(i)
    i.thumbnail(output_size, Image.Resampling.LANCZOS)
    i.save(picture_path)

    return picture_fn


def save_product_picture(form_picture):
    '''
    Input: Picture product image file from user form
    - Convert input picture to 500x500
    - Save it with random hex(10) name
    
    Return: Saved image name
    '''
    random_hex = secrets.token_hex(10)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/item_pics', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i = ImageOps.exif_transpose(i)
    i.thumbnail(output_size, Image.Resampling.LANCZOS)
    i.save(picture_path)

    return picture_fn
