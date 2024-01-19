import os
from pathlib import Path
import random
import shutil

folder_path = Path(f"./dataset_frame")
dataset= "frame"

filenames = os.listdir(str(folder_path))
# shuffle the filenames
random.shuffle(filenames)

os.makedirs(f"{dataset}")
folder_count=1

folder_now = Path(f"./{dataset}/{dataset}_{folder_count}/")
os.makedirs(name=str(folder_now))
for index, fn in enumerate(filenames):
    shutil.move(src=str(folder_path) + '/' +  fn, dst=str(folder_now) + "/" + fn)
    if ((index %5000 ==0) and (index != 0)) or (index == len(filenames)-1):
        print(f"at index : {index}")
        folder_count += 1
        folder_now = Path(f"./{dataset}/{dataset}_{folder_count}/")
        os.makedirs(name=str(folder_now))
