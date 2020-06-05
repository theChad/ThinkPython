import random
import analyze_book

# Exercise 13.8

# 13.8.1
def read_wordlist(filename="book.txt"):
    """Read wordlist from filename
    """
    words = []
    fin = open(filename)
    for line in fin:
        words.extend(line.split())
    return words


def create_prefix_map(filename="book.txt", len_prefix=2, len_suffix=1):
    """Create a dictionary of prefixes to possible suffixes from 
    any prefix
    """
    words = read_wordlist(filename)
    prefix_map = dict()
    # Store prefix and suffix lengths in prefix map
    prefix_map[None] = [len_prefix, len_suffix]
    for i in range(len(words)-len_prefix-len_suffix+1):

        
        # Put the first len_prefix words at this point into prefix,
        # and the next len_suffix words into suffix. Make them tuples, so
        # we can use them as keys for dictionaries and sets.
        prefix = tuple(words[i:i+len_prefix])
        suffix = tuple(words[i+len_prefix:i+len_prefix+len_suffix])

        # Using sets for suffixes. If we haven't encountered this prefix before,
        # initialize with an empty dictionary. Do setdefault on *that* dictionary
        # also, to build up a histogram of suffixes. An entry might look like
        # {('this', 'is'):
        #      {('a',): 34, ('the',): 23, ('my'): 10}}
        # The keys (prefixes and suffixes) are all tuples. A tuple with length one
        # is written like (<value>,).
        suffix_hist = prefix_map.setdefault(prefix, {})
        suffix_hist[suffix] = suffix_hist.get(suffix, 0) + 1
        #prefix_map.setdefault(prefix, {})[suffix] = (suffix,0) += 1
    return prefix_map

# 13.8.2

def generate_random_text(prefix_map, num_words_to_generate=100):
    """Generate random text from a dictionary of prefixes to suffixes
    """
    # We've stored the prefix and suffix lengths in the map.
    # Get those, then delete the entry so we don't run into
    # it when picking random prefixes
    len_prefix = prefix_map[None][0]
    len_suffix = prefix_map[None][1]
    del(prefix_map[None])

    # Get all prefixes so we can choose one at random when no
    # possible suffixes exist.
    prefix_list = list(prefix_map.keys())
    
    generated_text = random.choice(prefix_list)
    i=0
    while i < num_words_to_generate:
        # Get a prefix from the text generated so far
        prefix = generated_text[i:i+len_prefix]
        # Only try to generate the suffix if the prefix is
        # in our prefix map.
        if prefix in prefix_map:
            # Generate a random suffix from the possiblities
            # choose_from_hist, from analyze_book.py, choose items
            # randomly based on a histogram. It returns them as a list,
            # one item in our case, so we'll use [0] to get the item.
            # Which will be a tuple of the suffix word(s), of length
            # len_suffix.
            suffix = analyze_book.choose_from_hist(prefix_map[prefix])[0]
            generated_text+=suffix
            i += len(suffix)
        # If prefix is not in the map, generate a new prefix.
        # I think this should only happen if we reached unique
        # text at the very end of the original file. E.g. 'The End.'
        # No suffix to predict after that.
        else:
            new_text = random.choice(prefix_list)
            generated_text+=new_text
            i += len(new_text)
    generated_text_string = ' '.join(generated_text)
    return generated_text_string

def test_markov():
    text = generate_random_text(create_prefix_map('double.txt',2,1),1000)
    print(text)
    
if __name__=='__main__':
    test_markov()
