# Section 14.4 Exercise

import os

def print_walkthrough(top_dir=""):
    """Recursively print names of all files in top_dir
    """

    # Allow user to input directory to start from if function
    # called with no argument.
    if top_dir=="":
        top_dir = input("Which directory?\n")
    all_files=[]

    # Each iteration of os.walk gives a 3-tuple. We'll only
    # be using files,
    for root, dirs, files in os.walk(top_dir):
        all_files.extend(files) # Build up list of all files
    print(all_files)


if __name__=='__main__':
    print_walkthrough()
