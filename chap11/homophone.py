# Exercise 11.6

# is_candidate and has_homphones will check if dropping each of the first
# two letters results in words, and if those words are distincy homophones.
# Together these two functions determine if a word is a solution to the problem.
#
# find_homphones uses those checks to run through all the words.

# The one word returned was scent (and llama, before I required uniquness).


import pronounce, worddict

def is_candidate(wordlist, word):
    """True if word is a candidate for the homophone problem, in that
    it's five letters long, and removing either of the first two
    letters also results in a word.
    wordlist: dictionary of words
    word: string
    """
    word1 = word[1:]
    word2 = word[0]+word[2:]
    # Python evaluates and clauses left to right, so `p and q and r` is like
    # saying if p, then if q, then if r, return true. Otherwise return false.
    return len(word)==5 and word1 != word2 and word[1:] in wordlist and \
        word[0]+word[2:] in wordlist

def has_homophones(pro, word):
    """True if word can drop either of first two letters and get a homophone
    both ways.
    pro: dictionary of pronuncations
    word: string
    """
    if not (word in pro and word[1:] in pro and word[0]+word[2:] in pro):
        return False
    return pro[word]==pro[word[1:]]==pro[word[0]+word[2:]]

def find_homophones(pronounce_file="c06d", word_file="../chap9/words.txt"):
    """Find homophones specifically related to this problem. 5 letter word,
    dropping either of the first two characters yields a homophone.
    pronunce_file: location of file holding CMU Pronunciation Database
    word_file: long list of words
    """
    wordlist = worddict.make_dict(word_file)
    pro = pronounce.get_dictionary(pronounce_file)
    candidates = []
    # Search words. If it's a solution (check if dropping either of the
    # first two letters results in a word both times, and then
    # if those words are distincty homophones), append it to candidates.
    for word in wordlist:
        if is_candidate(wordlist, word) and \
           has_homophones(pro, word.upper()):
            candidates.append(word)
    return candidates


