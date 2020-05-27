# Exercise 9.1

def big_words(filename = "words.txt"):
    """Open filename and print out all words longer than 20 characters.
    """
    fin = open(filename)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

#big_words()

# Exercise 9.2
# 33.07% of words have no e (37,641).

def has_no_e(word):
    """Return true if word has no e, and false otherwise
    word: a string
    """
    # find is a string method that returns the first location
    # of its argument in the string. If it doesn't find it, it
    # returns -1.
    # x==a will return true if x is equal to a, and false otherwise.
    return word.find('e')==-1

def no_e_words(filename = "words.txt"):
    """Print out all words in filename with no 'e'
    """
    fin = open(filename)
    count = 0 # no e words
    total_count = 0 # all words
    for line in fin:
        word = line.strip()
        total_count += 1
        if has_no_e(word):
            print(word)
            count += 1
    print("Percentage of words with no e:",100*count/total_count)
            
#no_e_words()

# Exercise 9.3
# 'kqvxz' excludes 24667 words (keeps 89142)

def avoids(word, forbidden):
    """ Predicate that asks whether word avoids letters in the forbidden string
    """
    # Feels like there should be a more efficient way to do this using
    # set intersection, but I'll just check the word character by character
    for letter in forbidden:
        if word.find(letter)!=-1:
            return False
    return True

def number_of_avoiders(filename="words.txt"):
    """Print the number of words that avoid all letters input by the user.
    """
    forbidden = input("Reveal the forbidden string: ")
    count = 0 # intialize the count of words to zero
    fin = open(filename)
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            count += 1 # Found an avoider, increment count
    print("There are", count, "avoiders.")
    return count

#number_of_avoiders()

# Exercise 9.4

def uses_only(word, allowed):
    """Predicate that asks whether word *only* uses letters allowed string.
    word: string to be searched
    allowed: string of allowed letters
    """
    # This is a set intersection problem again, but I'll use string methods.
    # Cycle through letters in word this time
    for letter in word:
        # If a letter in word is not in allowed, it's not obeying the rules
        # so we need to return False
        if allowed.find(letter)==-1:
            return False
    return True

# Exercise 9.5
# 598 words use 'aeiou'
# 42 words use 'aeiouy'

def uses_all(word, required):
    """Predicate which asks whether word uses *all* letter in required string.
    word: string to be searched
    required: string, word must use all letters in this string to be true
    """
    # Sort of the converse of uses_only; this time if any letter in required
    # is not found in word, we return false.
    for letter in required:
        if word.find(letter)==-1:
            return False
    return True


# Writing this function to help test other functions.
# Searches through filename and prints out words that satisfy the predicate.
# A predicate is a function that takes one argument (I'm sort of fudging that here I
# guess, but think of the second string as part of the predicate) and returns true or false,
# like most of the functions here.

def filter_words(pred, filter_string=None, filename = "words.txt"):
    """Filters words in filename using the function predicate. 
    Will call pred(word, filter_string) or simply pred(word) if no
    filter_string is provided
    pred: predicate function to filter out words
    filter_string: second argument to pred
    """
    count = 0
    # Make a true predicate function, folding in the filter_string if there was one.
    # I want this so when I run through all lines in words.txt, I can just check
    # true_pred(word), without having to worry about whether I also need to pass
    # in the filter string.
    if filter_string==None:
        # No filter string, so our true_pred fuction will really just be a pass-through
        # for pred, which could be has_no_e or is_abecedarian
        def true_pred(word):
            return pred(word)
    else:
        # Else case. So there *is* a filter string. I want to be able to filter without
        # referring to the filter string, so true_pred is now a "wrapper" around
        # another fuction, with that extra argument already in there
        # pred here might be avoids, uses_only or uses_all
        def true_pred(word):
            return pred(word, filter_string)
    fin = open(filename)
    for line in fin:
        word = line.strip()
        if true_pred(word):
            print(word)
            count +=1
    print("Found", count, "words")

# Exercise 9.6
# 596 words are abecedarian

def is_abecedarian(word):
    """Is word written in alphabetical order?
    """
    # Make it all lower case, just in case
    word = word.lower()
    for i in range(len(word)-1):
        # if this letter is greater than (further in the alphabet) the next,
        # it's not in alphabetical order so just return False now
        if word[i]>word[i+1]:
            return False
    return True # Nothing broke the rules, so return True
