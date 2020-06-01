# Exercise 12.3

# Metathesis pairs will be anagrams. So we can use the anagram dictionary
# from the previous problem, checking among anagrams for metathesis pairs.

import anagram_sets

# First write a function to test for meta pairs
def is_meta_pair(word1, word2):
    """Return true if word1 and word 2 are metathesis pairs, i.e. if
    you can transform one into the other by switching two letters.
    word1, word2: string
    """
    # Run through ever pair of letters in word1. Take the first letter and
    # the second, first and third, ...then second and third, second and fourth...
    # Check the letter-swapped version of word1 vs word2, and if they're the
    # same return True.
    for i in range(len(word1)-1):
        for j in range(i+1, len(word1)):
            # Create a new word formed by swapping the ith and jth letter of word1
            test_word = word1[:i]+word1[j]+word1[i+1:j]+word1[i]+word1[j+1:]
            if test_word == word2:
                return True
    return False

# Now for a list of lists of all meta pairs.
def find_meta_pairs(anagram_dict):
    """Find metathesis pairs from a dictionary whose values are lists
    of anagrams
    anagram_dict: dictionary
    """
    meta_pairs=[]
    # For each list of anagrams (word_list), check all the words
    # against each other. Start by checking the first word against
    # the second and beyond. Then check the second word against
    # the third and beyond, etc. If it's a meta pair, append the pair
    # to the growing list of meta pairs.
    for word_list in anagram_dict.values():
        for i in range(len(word_list)):
            for j in range(i+1, len(word_list)):
                if is_meta_pair(word_list[i], word_list[j]):
                    meta_pairs.append([word_list[i], word_list[j]])
    return meta_pairs

if __name__=='__main__':
    print("test")
    meta_pairs = find_meta_pairs(anagram_sets.get_anagrams())
    print(meta_pairs)



