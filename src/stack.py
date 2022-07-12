import os
from os import listdir, chdir
from os.path import isfile, join
import numpy as np
from PIL import Image
import nibabel as nib
from skimage.transform import resize
import time


def to_array(dir):

    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    stk = []
    for img in files:
        img = join(dir, img)
        im = Image.open(img).convert("F")
        arr = np.array(im)
        arr = resize(arr, (360, 360))
        stk.append(arr)

    stack = np.stack(stk, axis=2).astype(np.float32)
    return stack


def to_nifti(dir_list):
    for name, dir in dir_list.items():
        arr = to_array(dir)
        arr = np.rot90(arr, k=1)
        new_image = nib.Nifti1Image(arr, affine=np.eye(4))
        folder = "nifti"
        if not os.path.exists(folder):
            os.makedirs(folder)
        nib.save(new_image, os.path.join(folder, name))
        print(f"Nifti Saved at {folder} under name: {name}")
