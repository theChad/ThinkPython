# Exercise 12.2

# Get a dictionary of the words
def get_anagrams(filename="../chap9/words.txt", num_letters=0):
    """Read words from filename into a dictionary. Key will be alphabetically
    arranged letter of the word, values will be a list of the words
    with those letters.
    num_letters: if greater than zero, restrict anagrams to only words
    with num_letters. For Exercise 12.2.3
    """
    anagrams = dict()
    fin = open(filename)
    for line in fin:
        word = line.strip()
        alpha_word = ''.join(sorted(word))
        # Use setdefault for the first time we try to use the key
        # alpha_word. anagrams[alpha_word] is set to [], and then appending
        # word makes anagrams[alpha_word]==[word]. Otherwise it's
        # [word1, word 2, .., word]
        anagrams.setdefault(alpha_word,[]).append(word)
    # Only want words with anagrams; make sure every entry has at least
    # two words. list(anagrams.items()) will force the iterator, which is
    # anagrams.items(), into a list. This is necessary so nothing
    # breaks when we delete items from the dictionary. If we just used
    # anagrams.items, which is a view directly into the dictionary,
    # it would get confused when we started deleting items in the object
    # it's looking at.
    for alpha_word, words in list(anagrams.items()):
        if len(words) < 2:
            del anagrams[alpha_word]
            
    # Remove words with the wrong number of letters, if necessary
    if num_letters!=0:
        for alpha_word, words in list(anagrams.items()):
            if len(alpha_word)!=num_letters:
                del anagrams[alpha_word]
    return anagrams

# Exercise 12.2.2
def anagrams_by_quantity(anagrams):
    """Given a dictionary whose values are lists of anagrams,
    return a dictionary keyed to the size of those lists
    anagrams: dictionary of anagrams
    """
    num_anagrams = dict()
    for words in anagrams.values():
        num_anagrams.setdefault(len(words),[]).append(words)
    return num_anagrams


# Print out all the anagrams from a dictionary
def print_anagrams(anagrams):
    """Print out anagrams from a dictionary where the values
    are unique lists of anagrams
    anagrams: dictionary
    """
    max_length = max(anagrams.keys())
    for i in range(max_length,1,-1):
        word_lists = anagrams.get(i,None)
        for words in word_lists:
            print(words)

# Exercise 12.2.3
# ANGRIEST

# I modified get_anagrams to take a num_letters component.
# It then filters out all words that don't satisfy it.
# The rest of the process is the same.
def scrabble_bingo():
    """Eight letters with most anagrams"""
    print_anagrams(anagrams_by_quantity(get_anagrams(num_letters=8)))

# Test functions
# The book's solutions use this, so I'll start using it too.
# I'm sure it'll explain it, but basically it means if someone runs
# this file specifically, e.g. through `python anagram_sets`,
# do all the things in this if statement.
# If I left out the if statment, it would still work fine when
# running this file, but if someone imported this file into another file,
# e.g. with `import anagram_sets` it would *also* run these little tests.
# Which would be wasteful at best, and likely cause errors (due to
# the default filename argument).
if __name__=='__main__':
    # Test finding all anagrams
    print_anagrams(anagrams_by_quantity(get_anagrams()))
    # Just scrabble words. I'll print them all, not just the first.
    print("Scrabble Words:")
    scrabble_bingo()
