import os
from os import listdir, chdir
from os.path import isfile, join
import numpy as np
from PIL import Image
import nibabel as nib


def to_array(dir):

    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    stk = []
    chdir(dir)
    for img in files:
        im = Image.open(img)
        arr = np.array(im)
        stk.append(arr)

    stack = np.stack(stk, axis=2).astype(np.float32)
    print(f"to array : {stack.shape}")
    return stack


def to_nifti(dir_list):
    print(f"to nifti")
    for dir in dir_list:
        arr = to_array(dir)
        arr = np.rot90(arr, k=1)
        new_image = nib.Nifti1Image(arr, affine=np.eye(4))
        print(f"nib save at {dir}")
        nib.save(new_image, filename="image")
