# Exercise 12.4
# complecting <-- largest reducible word in words.txt

# Using the hints..

# 12.4.4
# A bit backwards, but doing this first so we have the memo variable as global
known = dict()

# 12.4.1

def find_children(words, word):
    """Find all children of a word, i.e. words that are revealed
    by dropping a single letter.
    words: dictionary of words
    word: string
    """
    children = []
    for i in range(len(word)):
        possible_child = word[:i] + word[i+1:]
        if possible_child in words:
            children.append(possible_child)
    return children

# 12.4.2

def is_reducible(words, word, verbose=False):
    """True if a word is reducible, given a dictionary of words.
    words: dictionary
    word: string
    verbose: flag for printing out path of a single reducible word
    """
    # Base case. Empty string is reducible.
    if word=='':
        return True

    # Check memos
    if word in known:
        return known[word]
    
    # Cycle through children. If any is reducible, return True.
    for child in find_children(words, word):
        if is_reducible(words, child, verbose):
            known[word] = True # Set memo
            # This is just to print out all the words word reduces
            # down through.
            if verbose:
                print(word)
            return True
        
    # No reducible children. Word isn't reducible.
    known[word] = False # Set memo
    return False

# 12.4.3

def add_single_letter_words(words):
    """Add single letter words to the dictionary.
    """
    words['']=None
    words['i']=None
    words['a']=None
    return words

# Get dictionary of words from file
def get_words(filename="../chap9/words.txt"):
    fin = open(filename)
    words = dict()
    for line in fin:
        word = line.strip()
        words[word]=None
    return add_single_letter_words(words)

# Find all reducible words in dictionary
def find_reducible(words):
    """Find all reducible words in words. Return a new dictionary.
    words: dictionary
    """
    reducible=dict()
    for word in words:
        if is_reducible(words, word):
            reducible[word]=None
    return reducible

# Create new dictionary by length of keys of the old one
# to find the longest reducible words
def key_lengths(words):
    """Return a dictionary whose keys are numbers indicating word length.
    Their values will be a list of all words whose length is equal to that key.
    words: dictionary of words
    """
    word_length = dict()
    # For each word, add it to the appropriate entry (its length)
    # in word_length.
    for word in words:
        word_length.setdefault(len(word),[]).append(word)
    return word_length

# Find the maximum entry in a dictionary
def max_key(words):
    """Return the item with the maximum key in words.
    words: dictionary
    """
    return words[max(words.keys())]

# Find the biggest reducible word from words.txt
def find_reducible_from_file(filename="../chap9/words.txt"):
    words = get_words(filename) # Read in words (plus single letter words)
    reducible = find_reducible(words) # Dictionary of reducible 
    # Find all reducible words with the longest length
    biggest_reducibles = max_key(key_lengths(reducible))
    print(biggest_reducibles)

if __name__=='__main__':
    find_reducible_from_file()



