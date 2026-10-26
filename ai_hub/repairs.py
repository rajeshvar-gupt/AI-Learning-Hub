"""Bounded replacements inside the hub; legacy repositories remain unchanged."""
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
import numpy as np


def weather(city,key=None,transport=None):
    if not isinstance(city,str) or not 1<=len(city.strip())<=80:raise ValueError('city required')
    key=key if key is not None else os.getenv('OPENWEATHER_API_KEY','')
    if not key:raise ValueError('OPENWEATHER_API_KEY required')
    url='https://api.openweathermap.org/data/2.5/weather?'+urllib.parse.urlencode({'q':city,'appid':key,'units':'metric'})
    try:
        if transport is None:
            with urllib.request.urlopen(url,timeout=10) as response:value=json.load(response)
        else:value=transport(url)
    except (urllib.error.URLError,TimeoutError):raise RuntimeError('weather request failed') from None
    try:
        temp=value['main']['temp'];description=value['weather'][0]['description']
        if isinstance(temp,bool) or not isinstance(temp,(int,float)) or not np.isfinite(temp) or not isinstance(description,str):raise ValueError()
        return {'city':city,'temperature_c':temp,'description':description,'kind':'current observation; not an ML forecast'}
    except (KeyError,TypeError,IndexError,ValueError):raise ValueError('invalid weather response') from None


def pdf_text(path):
    from pypdf import PdfReader
    reader=PdfReader(path)
    text='\n'.join(page.extract_text() or '' for page in reader.pages).strip()
    if not text:raise ValueError('no extractable text; OCR is not implemented')
    return text


def image_lab(output='outputs/image-lab'):
    from PIL import Image,ImageFilter
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    # Original synthetic fixture, no camera/face data.
    pixels=np.zeros((64,64),dtype=np.uint8);pixels[16:48,20:44]=255
    image=Image.fromarray(pixels)
    image.save(output/'fixture.png')
    image.rotate(90).save(output/'rotated.png')
    image.filter(ImageFilter.FIND_EDGES).save(output/'edges.png')
    return {'shape':list(pixels.shape),'fixture':'original synthetic rectangle','outputs':['fixture.png','rotated.png','edges.png']}
