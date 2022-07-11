import os
from os import listdir, chdir
from os.path import isfile, join
import numpy as np
from PIL import Image
import nibabel as nib


def to_array(dir):

    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    stk = []
    for img in files:
        img = join(dir, img)
        im = Image.open(img)
        arr = np.array(im)
        stk.append(arr)

    # check if shapes match
    # why is there 3 extra channels
    stack = np.stack(stk, axis=2).astype(np.float32)
    print(f"to array : {stack.shape}")
    return stack


def to_nifti(dir_list):
    print(f"to nifti")
    for name, dir in dir_list.items():
        arr = to_array(dir)
        arr = np.rot90(arr, k=1)
        new_image = nib.Nifti1Image(arr, affine=np.eye(4))
        nib.save(new_image, name)
