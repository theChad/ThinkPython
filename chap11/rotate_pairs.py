# Exercise 11.5

# Ignore all of this, it's just so I can import caesar.py from the chapter 8 folder.
# I think it's pretty hacky.
# If the file caesar.py is in the same directory as this file, it's not necessary.
#--------------------------------------------------------------------------------
import os, sys
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR=os.path.split(CURR_DIR)[0]
NEW_DIR = os.path.join(PARENT_DIR,'chap8')
sys.path.append(NEW_DIR)
NEW_DIR = os.path.join(PARENT_DIR,'chap10')
sys.path.append(NEW_DIR)
#--------------------------------------------------------------------------------

import caesar, wordlist
import time

# I'll create a dictionary whose keys are every rotated word formed by
# any element of the wordlist (except the word itself),
# and whose values are the word(s) that can
# rotate to that value. Then go through the wordlist again and see if any
# words are keys to the dictionary.
def find_rotate_pairs(t):
    """Find all rotate pairs in list of words t
    """
    rotated = dict()
    rot_pairs = dict()
    for word in t:
        for i in range(1,26):
            rot_word = caesar.rotate_word(word,i)
            rotated.setdefault(rot_word,[]).append(word)
    for word in t:
        if word in rotated:
            rot_pairs[word] = rotated[word]
    return rot_pairs

# This one works from the other direction, first creating a plain dictionary of
# the wordlist, then word by word, checking each rotation for membership
# in that dictionary. If word1 has a rotation in the wordlist, add
# that rotation to the rotated pairs dictionary, with word1 as key. Remove
# the rotated word from the wordlist, since we'll be finding all of its
# rotations via word1. After going through all 25 rotations of word1,
# remove it from the wordlist dictionary as well (since we've already found
# all of its rotations).
# This function is about the same speed, but slightly faster due to avoiding
# duplicate checks. The output is also more succinct, having only one
# entry for each rotational group.
def find2(t):
    """Different implementation
    """
    wordlist = dict()
    rot_pairs = dict()
    for word in t:
        wordlist[word]=[]
    for word in t:
        if word in wordlist:
            for i in range(1,26):
                rot_word = caesar.rotate_word(word,i)
                if rot_word in wordlist:
                    rot_pairs.setdefault(word,[]).append(rot_word)
                    del wordlist[rot_word]
            del wordlist[word]
    return rot_pairs
            
# Test with words.txt
def test_words():
    word_list = wordlist.list_append()
    t0 = time.time()
    find_rotate_pairs(word_list)
    t1 = time.time()
    find2(word_list)
    t2=time.time()
    print("find took",t1-t0) # 8.8 seconds
    print("find2 took",t2-t1) # 6.6 seconds

test_words()

def small_test():
    test_list = ["barn", "yard", "nope", caesar.rotate_word("barn",12), "mnod", "opqf"]
    t0 = time.time()
    print(find_rotate_pairs(test_list))
    t1 = time.time()
    print(find2(test_list))
    t2=time.time()
    print(t1-t0)
    print(t2-t1)

