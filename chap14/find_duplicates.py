# Exercise 14.3

# Per the Python docs, os.popen is deprecated, so I'm using subprocess instead.
import subprocess 
import walk # from exercise in section 14.4

def find_all_suffix_files(directory='.', suffix='.txt'):
    """Find all files with given suffix in directory, recursively
    directory: string, directory name. Relative to current
    suffix: string, suffix of files
    """
    # Using get_all_files from walk.py, get a list of all
    # files in the given directory and its subdirectories
    all_files = walk.get_all_files(directory)
    all_suffix_files = [] # Build up a list of files with suffix
    for file in all_files:
        # From string documentation, endswith is a string method
        # that returns true if the string ends with the argument
        if file.endswith(suffix):
            all_suffix_files.append(file)
    return all_suffix_files

def get_checksum(filename):
    """Return the md5 checksum of filename
    """
    # You could use popen here. I read about it, and subprocess is meant
    # to replace os.popen, so I used it instead.

    # First, run the command md5 sum with filename as input.
    # It's stored as a subprocess.CompletedProcess
    process = subprocess.run(['md5sum',filename], capture_output=True)
    
    # Use the method stdout from subprocess.CompletedProcess (seen in
    # the Python docs) to get the output. As seen in the book, md5sum will
    # output the checksum follwed by the filename. split() will put
    # those two elements into a list, and [0] will take the first element,
    # which will be the checksum.
    checksum = process.stdout.split()[0]
    return checksum

def get_duplicates(files):
    """Return a list of duplicates found in files.
    """
    checksums = {}
    # Create a dictionary of files, keyed by their checksum
    for f in files:
        checksum = get_checksum(f)
        checksums.setdefault(checksum,[]).append(f)
    # Create a list of lists of duplicate files. Only file lists
    # with more than one item need apply.
    duplicates = []
    for csum, file_list in checksums.items():
        if len(file_list)>1:
            duplicates.append(file_list)
    return duplicates

def no_diff(file1, file2):
    """True if the command diff comes up empty for file1 and file 2
    """
    # Using subprocess again. 
    process = subprocess.run(['diff',file1,file2], capture_output=True)
    # Subprocess outputs bytes objects to stdout. If diff doesn't find
    # anything, it outputs an empty string. As a bytes object, that
    # is b''.
    if process.stdout==b'':
        return True
    return False

def check_duplicates(files):
    """True if all files in list of files are duplicates using diff
    files: list of filenames
    """
    # If we don't have two files, it's kind of meaningless. True or False
    # would be fine.
    if len(files) < 2:
        return True
    file1 = files[0]
    # Compare every file to the first file. If they're all the same, they're
    # all duplicates. If any one of them isn't, they're not all duplicates
    # so return False.
    for f in files[1:]:
        if not no_diff(file1, f):
            return False
    return True

def check_all_duplicates(duplicate_list):
    """Returns all lists of candidate duplicates that aren't actually duplicates
    duplicate_list: list of lists of duplicates
    """
    non_dupes = []
    for dupes in duplicate_list:
        if not check_duplicates(dupes):
            non_dupes.append(dupes)
    return non_dupes

def get_all_suffix_duplicates(directory='.', suffix='.txt'):
    """Get all duplicates of a given suffix in direcotry and its subdirectories
    directory, suffix: strings
    """
    all_suffix_files = find_all_suffix_files(directory)
    duplicates = get_duplicates(all_suffix_files)
    return duplicates


def test_duplicates():
    all_suffix_files = find_all_suffix_files('..')
    duplicates = get_duplicates(all_suffix_files)
    print("All files with suffix:")
    print(all_suffix_files)
    print("\nJust the duplicates")
    print(duplicates)
    print("\nDupes again")
    print(get_all_suffix_duplicates('..'))
    print("Of those, these aren't duplicates:")
    print(check_all_duplicates(duplicates))

if __name__=='__main__':
    test_duplicates()
