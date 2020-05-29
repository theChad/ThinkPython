# Function to read in the CMU file of words and their pronunciations

def get_dictionary(filename="c06d"):
    """Return a dictionary of the words and their pronunciations
    from the CMU Pronouncing Dictionary.
    Each pronunciation will be a string.
    """
    pro = dict() # initialize word-pronuncation dictionary
    fin = open(filename)
    for line in fin:
        if line[0]=='#':
            continue # Like a soft break; jump straight back to top of loop
        # Kind of a shorcut for assigning a list to multiple
        # items. The same end result as the two commands
        # word = line.split("  ")[0]
        # pronounce = line.split("  ")[1]
        # The first space on each line of data is between the word
        # and its pronunciation. 
        [word, pronounce] = line.split(" ",1)
        pro[word]=pronounce.strip()
    return pro
        
