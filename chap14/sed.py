# Exercise 14.1

def sed(pattern, replacement, filename1, filename2):
    """Write contents of file1 into file2, replacing any occurrence
    of pattern with replacement.
    pattern, replacement: strings
    filename1, filename2: strings, names of files
    """

    fin = open(filename1) # open the normal way
    fout = open(filename2, 'w') # open for writing (create if not there)

    for line in fin:
        # replace is a string method that replaces instances of
        # the first argument with the second, returning a new string
        fout.write(line.replace(pattern, replacement))

    fin.close()
    fout.close()

def test_sed():
    sed('marshmallows', 'cat hair', 'f1.txt', 'f2.txt')

if __name__=='__main__':
    test_sed()
