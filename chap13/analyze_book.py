import string, random

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

# Different words used in book
def unique_words(book):
    """Count unique words used in book, from histogram
    book: histogram of words in book
    """
    return len(book)

# Total words in book
def total_words(book):
    """Count total words in book histogram
    """
    return sum(book.values())
        
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
    Convert words to lowercase. Return a dictionary of words
    and their frequencies, a histogram.
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
    word_freqs: dictionary of words with frequency values, histogram
    """
    top = dict()
    num_words = 0 # keep track of how many words we've found
    # Get all keys (which are frequencies) in reverse order
    freqs = sorted(word_freqs.keys(), reverse = True)

    # freqs is in order from high to low, so get the first
    # n entries to find the n highest words
    for i in range(n):
        # list of words with frequency i
        words = word_freqs[freqs[i]]
        # Forming dictionary of top words by adding this entry,
        # with the frequency
        top[freqs[i]] = words
        # Since we do have lists of words, and several words may
        # have the same frequency, we probably don't need to go
        # through n frequencies to find n words.
        # num_words keeps track of how many words we've added to
        # top so far. If it's at least n, we're done
        num_words += len(words)
        if num_words >= n:
            break
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

# Test 13.1-4
def test_book_analysis():
    words = get_only_words('kafka.txt') 
    top_words = get_top_words(invert_dict(words))
    print("Uniqe words used:", unique_words(words), "out of",
          total_words(words), "total words.")
    print("Top words:\n", top_words)
    non_words = check_wordlist(get_word_list(), words)
    print("These aren't words:\n", non_words.keys())



# Exercise 13.5
# The book's version of choose_from_hist is much simpler. This one
# requires a much smaller list (just all unique words, vs all words),
# I think this version should be faster, and it requires less memory.
# But it's still on the same order of time complexity - doubling
# the text will probably take twice the time for each of these.
# Until the number of new unique words tops growing, and then
# this version stops taking much more time at all.

# Overview of book's version:
# Create a list of every single word in the book, with repeats.
# Effectively, that's the same as just reading the book directly into a list,
# e.g. ['once', 'upon', 'a', 'time', 'a']. Now randomly
# pick an element of that list (you can see 'a' is twice as likely to be
# chosen as any other element).

# Overview of this version:
# Make a histogram of cumulative frequencies. Order doesn't really matter.
# So from the above sample text, it would look like
# {'once': 1, 'upon': 2, 'a': 4, 'time':5}. Now randomly pick a number
# from 1 to 5, and pick a word by its cumulative frequency. The lowest
# cumulative frequency that's greater than or equal to the random number.
# If you pick 1, you return 'once'. 2, 'upon'. 3 or 4, 'a'. 5, 'time'.
# So again 'a' is twice as likely as any other element.


# This will be used to search my list of cumulative frequencies
# quickly to determine which word has been picked out by the
# random number generated
def binary_search(sorted_list, target):
    """Find where a number lies in a sorted list. Return lowest item
    that is greater than or equal to target, or None if no item
    in list greater than or equal to target
    """
    if sorted_list==[]:
        return None
    if len(sorted_list)==1:
        if target <= sorted_list[0]:
            return 0
        return None
    mid_index = int(len(sorted_list)/2)-1
    mid_value = sorted_list[mid_index]
    if target <= mid_value:
        return binary_search(sorted_list[0:mid_index+1], target)
    else:
        return mid_index + 1 + binary_search(sorted_list[mid_index+1:], target)
    
    
def choose_from_hist(hist, n=1):
    """Choose elements randomly from histogram hist, with 
    probability equal to the frequency of those elements.
    Return a list of words
    hist: histogram dictionary
    n: integer, number of words to generate
    """
    counter = 0
    c_freqs = []
    c_values = []
    # Create two lists, one of cumulative frequency and the other of words.
    # This is a substitute for the histogram described above in the
    # 'once upon a time a' example. Two lists, side by side,
    # instead of one dictionary.
    # c_freqs[i]-c_freqs[i-1] will be the frequency of c_values[i]
    for entry, freq in hist.items():
        counter += freq
        c_freqs.append(counter)
        c_values.append(entry)
    # Randomly choose a number from 1 to counter, and place it in the
    # appropriate bucket based on the cumulative frequency. Words with
    # higher frequency will have bigger buckets and thus be more likely
    # to be picked.
    chosen_ones = []
    for i in range(n):
        random_number = random.randint(1, counter)
        # Find the index of the bucket random_number falls into
        # binary_search will look through the cumulative frequencies we
        # pass it and find the i that makes
        # c_freqs[i-1] < random_number <= c_freqs[i].
        # Or 0, if random_number <= c_freqs[0]
        chosen_index = binary_search(c_freqs, random_number)
        chosen_word = c_values[chosen_index]
        chosen_ones.append(chosen_word)
    return chosen_ones
    
# Test 13.5

def test_histogram():
    """Test the choose_from_hist function
    """
    print("\nHere's a hundred random words from the text.")
    hist = get_only_words('kafka.txt')
    print(choose_from_hist(hist, 100))
                               

                        

if __name__=='__main__':
    test_book_analysis()
    test_histogram()
    pass
    
