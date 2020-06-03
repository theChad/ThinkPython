import string

# Exercise 13.1
# I didn't use translate. I search the strings for the offending
# characters one by one.

# General function I can use to create the punctuation and whitespace functions below.
def remove_chars(s, chars):
    """Remove any character in chars from string s
    s: string
    chars: string of characters
    """
    for c in chars:
        if c in s:
            s = s.replace(c,'')
    return s

def remove_punctuation(s):
    """Remove punctuation from s
    """
    s=remove_chars(s,string.punctuation)
    return s

def remove_whitespace(s):
    """Remove punctuation from s
    """
    s=remove_chars(s,string.whitespace)
    return s

# Don't count words in the header portion
def skip_header(fin):
    """Skip header of project gutenberg file
    """
    for line in fin:
        if line[:3]=='***':
            return fin

# Exercise 13.3
# Copied over from Chapter 11
def invert_dict(d):
    """Return a dictionary whose keys are the values of d, and whose
    values are lists of the corresponding keys of d
    """
    inverse = dict()
    for key in d:
        val = d[key]
        # If val is in inverse, setdefault(val,[]) will just return
        # inverse[val], so this is like saying inverse[val].append(key).
        # If val is *not* in inverse, setdefault will create the key-value
        # pair {val: []}, then return inverse[val] (which is now []).
        # Then we call append(key) on this new inverse[val], which will yield
        # inverse[val]=[key]
        inverse.setdefault(val,[]).append(key)
    return inverse


def get_only_words(filename="book.txt"):
    """Strip whitespace and punctation from words in file.
    Convert words to lowercase.
    """
    fin = open(filename)
    words = dict()
    fin=skip_header(fin)
    for line in fin:
        # Remove punctuation from line first
        line = remove_punctuation(line)
        # split returns a list of the words in line, split across
        # whitespace
        words_in_line = line.split()
        for word in words_in_line:
            word = word.lower() # make word lowercase
            words[word] = words.get(word,0) + 1 # Increment frequency count
    return words

# Exercise 13.3

def get_top_words(word_freqs, n=20):
    """Get top n entries from word_freqs
    word_freqs: dictionary of frequencies
    """
    top = dict()
    # Get all keys (which are frequencies) in reverse order
    freqs = sorted(word_freqs.keys(), reverse = True)
    for i in range(n):
        top[freqs[i]] = word_freqs[freqs[i]]
    return top

# Exercise 13.4

def get_word_list(filename="../chap9/words.txt"):
    """Read in a wordlist, return dictionary of the words
    """
    fin = open(filename)
    word_dict = dict()
    for line in fin:
        word = line.strip()
        word_dict[word]=None
    return word_dict

def check_wordlist(word_list, book_words):
    """Check book_words against word_list to see if there are any
    non-words in book_words.
    """
    non_words = dict()
    # Checking every key of book_words to make sure it's in word_list
    # For a new dictionary, non_words, along the way
    for word in book_words:
        if not (word in word_list):
            non_words[word] = None
    return non_words


if __name__=='__main__':
    words = get_only_words('kafka.txt') 
    top_words = get_top_words(invert_dict(words))
    print("Total words used:", len(words))
    print("Top words:\n", top_words)
    non_words = check_wordlist(get_word_list(), words)
    print("These aren't words:\n", non_words.keys())
