# Exercise 14.2

# This code just allows me do a relative import from another folder
import os, sys
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.split(CURR_DIR)[0]
NEW_PATH = os.path.join(PARENT_DIR, 'chap12')
sys.path.append(NEW_PATH)
# End of relative import code

import shelve
import anagram_sets

def store_anagrams(anagram_dictionary, filename='anagrams.db'):
    """Use shelves to store anagram_dictionary in filename.
    anagram_dictionary: dictionary of sorted letters, with a list
    of anagrams as a value
    filename: string
    """
    # As shown in an example in the documentation, I'm using
    # context management here. It essentially just opens and closes
    # things for you
    with shelve.open(filename) as db:
        db['anagram_dictionary'] = anagram_dictionary

def read_anagrams(word, filename='anagrams.db'):
    """Read the anagram dictionary from a file, and return all
    anagrams of word
    word: string
    filename: string, location of database with anagram dictionary
    """
    # First alphabetize the letters of word, so we can look it up
    alpha_word = ''.join(sorted(word))

    # Now open the database using context managment (with..as).
    # It will open filename into a database and call it db.
    with shelve.open(filename) as db:
        # db['anagram_dictionary] is the anagram dictionary
        # We then index that with the key alpha_word to et
        # our list of anagrams
        anagram_dictionary = db['anagram_dictionary']
        anagrams = anagram_dictionary.get(alpha_word,[word])
    return anagrams

# Function to test storing and reading anagrams
def test_anagrams():
    """Test store_anagrams and read_anagrams.
    """
    anagram_dictionary = anagram_sets.get_anagrams()
    print("Storing anagrams..")
    store_anagrams(anagram_dictionary)
    print("Reading anagrams..")
    # Read in a word from the user and print out all
    # anagrams of that word. Continue until user enters
    # a blank line.
    word = input()
    while word != '':
        print(read_anagrams(word))
        word = input()

if __name__=='__main__':
    test_anagrams()
