# Section 14.4 Exercise

import os

def get_all_files(top_dir=""):
    """Recursively collect names of all files in top_dir
    """

    # Allow user to input directory to start from if function
    # called with no argument.
    if top_dir=="":
        top_dir = input("Which directory?\n")
    all_files=[]

    # Each iteration of os.walk gives a 3-tuple. We'll use root and files
    # to get a full filepath for each file
    for root, dirs, files in os.walk(top_dir):
        # This is called a list comprehension. It's not covered
        # until the end of the book, but it's a useful tool.
        # You can read about them in the python documentation, or in the book.
        # In this case, the next line is a short cut for the following.
        # for i in range(len(files)):
        #     files[i] = os.path.join(root, files[i])
        filepaths = [os.path.join(root, file) for file in files]
        
        # Add the new list of files in this directory to our list of all files
        all_files.extend(filepaths)

    return all_files

def print_walkthrough():
    print(get_all_files())


if __name__=='__main__':
    print_walkthrough()
