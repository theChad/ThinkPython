# Exercise 11.1

def make_dict(filename="../chap9/words.txt"):
    """Return dictionary of words in filename
    """
    words = dict()
    fin = open(filename)
    for line in fin:
        word = line.strip()
        words[word] = ""
        
