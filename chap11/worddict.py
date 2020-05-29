# Exercise 11.1

def make_dict(filename="../chap9/words.txt"):
    """Return dictionary of words in filename
    """
    words = dict()
    print("Calling worddict.make_dict on", filename)
    fin = open(filename)
    for line in fin:
        word = line.strip()
        words[word] = ""
    return words
        
