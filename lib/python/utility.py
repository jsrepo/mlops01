from io import BytesIO
from PIL import Image
import numpy as np
import pandas as pd
import cv2


def process_images(in_folder, out_folder, func, args=[], func_type='opencv'):
    out_folder.clear()
    for path in in_folder.list_paths_in_partition():
        image = open_image(path, in_folder, out_type=func_type)
        image = func(image, *args)
        save_image(image, path, out_folder, in_type=func_type)
         
def analyse_images(in_folder, func, args=[], func_type='opencv'):
    data = []
    for path in in_folder.list_paths_in_partition():
        image = open_image(path, in_folder, out_type=func_type)
        data.extend([[path] + [infos] for infos in func(image, *args)])
    return data

def open_image(path, folder, out_type='opencv'):
    with folder.get_download_stream(path) as stream:
        raw_img_bytes = stream.read()
        img = Image.open(BytesIO(raw_img_bytes))
    if out_type == 'opencv':
        return np.array(img.convert('RGB'))
    else:
        return img.convert('RGB')


def save_image(image, path, folder, in_type='opencv'):
    if in_type == 'opencv':
        image = Image.fromarray(image)
    else:
        image = Image.fromarray(np.array(image.convert('RGB')) )
    buf = BytesIO()
    image.save(buf, format='JPEG')
    processed_img_bytes = buf.getvalue()
    folder.upload_data(path, processed_img_bytes)

def pil_to_cv(pil_image):
    open_cv_image = np.array(pil_image.convert('RGB')) 
    return open_cv_image

def cv_to_pil(open_cv_image):
    pil_image = Image.fromarray(open_cv_image)
    return pil_image

def notebook_display(image):
    from IPython.display import Image as Img, display
    path = 'viz.jpg'
    cv2.imwrite(path, image)
    display(Img(filename=path))

#def iterfiles(folder):
#    folder_path = folder.get_info()['path']
#    path_list = [folder_path + file_path for file_path in sorted(folder.list_paths_in_partition())]
#   return path_list