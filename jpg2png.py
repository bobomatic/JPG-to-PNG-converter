"""
jpg2png input_folder output_folder(optional)
Converts a jpg file to PNG
e.g.
python3 jpg2png.py Pokedex/ converted/
"""

import sys
import os
from PIL import Image


def convert(input_folder, output_folder):
    # loop through folder
    filenames = os.listdir(input_folder)
    for filename in filenames:
        if filename.endswith(".jpg"):
            in_file_path = os.path.join(input_folder + filename)
            out_file_path = os.path.join(output_folder + os.path.splitext(filename)[0]) + '.png'
            img = Image.open(in_file_path)
            print('converting...', in_file_path, 'to', out_file_path)
            # converted_img = img.convert('L') #convert to grayscale - not used
            converted_img = img
            converted_img.save(out_file_path, 'png')
    return 'Done'


# grab first and second argument of command line using sys
try:
    input_path = sys.argv[1]
    try:
        output_path = sys.argv[2]
    except IndexError:
        output_path = 'converted/'

    # create a folder
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # convert files in folder
    print(convert(input_path, output_path))

except IndexError:
    print('Please specify input folder')
