from pathlib import Path
from PIL import Image
import os
import pyheif
import datetime

def save_image(image_file, save_path, image_number=0):
    # save_path = save_path.with_suffix(".jpg")
    image_file.save(save_path, "JPEG")
    
def new_name_with_date_number(image_filepath,number=0,gauge=None):
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date().strftime("%Y_%m_%d")
    new_name = current_date 
    if gauge is not None:
        new_name = new_name + f"_{gauge}"
    new_name = new_name + f"_{number}"
    
    new_image_filepath = image_filepath.with_name(new_name).with_suffix(image_filepath.suffix)
    # print(new_image_filepath)
    
    return new_image_filepath

def rename_image(source="", dest=""):
    os.rename(src=str(source), dst=str(dest))

def delete_image(path):
    os.remove(str(path))

# folder_path_list = [ Path(f"./frame/frame_{i}/") for i in range(1,13,1)]
folder_path_list = [Path(f"./frame/frame_1/")]
gauge = "digital"

for folder_path in folder_path_list:
    start=0
    files = [f for f in os.listdir(folder_path)]
    for count, filename in enumerate(files):
        image_number = start + count + 1
        image_filepath = folder_path / filename
        new_image_filepath = new_name_with_date_number(image_filepath,number=image_number,gauge=gauge)
      
        # print(str(new_image_filepath))
        # if count == 20:
        #     break
        
        rename_image(source=image_filepath, dest=new_image_filepath)
        
        # if str(image_filepath).lower().endswith(('.png', '.jpg', '.jpeg')):
        #     rename_image(source=image_filepath, dest=new_image_filepath)
        # else:
        #     # print(f"--- NOT : {image_filepath.suffix} ---")
        #     if (str(image_filepath.suffix) == ".HEIC") or (str(image_filepath.suffix) == ".heic"):
        #         heic_file_path = image_filepath
        #         heic_file = pyheif.read(heic_file_path)
        #         image = Image.frombytes(
        #             heic_file.mode,
        #             heic_file.size,
        #             heic_file.data,
        #             "raw",
        #             heic_file.mode,
        #             heic_file.stride
        #         )
                
        #         save_image(image_file=image, save_path=new_image_filepath,image_number=image_number)
        #         delete_image(path=image_filepath)
                
        #     elif str(image_filepath.suffix) == ".webp":
        #         print(f"webp format")
        #         rename_image(source=image_filepath, dest=new_image_filepath)
        #     else:
        #         print(f"++++++++++++++++++++++ another format : {image_filepath.suffix} ++++++++++++++++++++++")
        #         rename_image(source=image_filepath, dest=new_image_filepath)
        
