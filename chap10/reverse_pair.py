# Exercise 10.11

import wordlist
import inlist


def reverse_in_list(words, word):
    """True if the reverse of word is in the list words
    """
    rev_word = word[::-1]
    return inlist.in_bisect(words,rev_word)


def reverse_pairs(words):
    """Return a list of all words that are part of a reverse pair.
    words: list of words to search
    """
    rev_pairs=[] # accumulator for the reversable words
    for word in words:
        # If the reverse of word is in the list, append word to
        # the list or reverse pair words
        if reverse_in_list(words, word):
            rev_pairs.append(word)
    return rev_pairs

def reverse_pairs_wordstxt():
    """Test reverse_pairs out on word.txt
    """
    words = wordlist.list_append()
    return reverse_pairs(words)
