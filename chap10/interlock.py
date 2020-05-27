# Exercise 10.12

import wordlist, inlist

def interlocked(words, word, layers=2):
    """Returns list of word and its components if word is 
    the result of interlocking two other words from list.
    Otherwise returns empty list
    words: list of words
    word: potential compound interlocked word
    layers: number of words to interlock. e.g. layers=2
    would interlock aaaa bbbb to get abababab
    """
    component_words = []
    # Form the component words (which may not be words)
    for i in range(layers):
        component_words.append(word[i::layers])
        # If the component word is in the list, keep going
        if inlist.in_bisect(words, component_words[i]):
            pass
        # If a component word is not in the list, this
        # word isn't interlocked. So just return [], which
        # would be read as False in a conditional.
        else:
            return []
    print(word,"from",component_words)
    return [word, component_words]

def find_interlocked(words, layers=2):
    """Find all words in a list which can be formed by 
    interlocking two other words.
    words: list of words
    layers: how many words interlock to form one new word
    """

    interlocked_words = []
    for word in words:
        word_interlocked = interlocked(words, word, layers)
        if word_interlocked:
            interlocked_words.append(word_interlocked)
    return interlocked_words


# Wrote this to test interlocked words on words.txt, but
# there are a lot of them
def find_interlocked_moby(layers=2):
    """Find all interlocked words in the Moby file words.txt
    """
    words = wordlist.list_append()
    find_interlocked(words,layers)
