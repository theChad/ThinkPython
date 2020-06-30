# Exercise from Section 18.10
# Refactored version of code from the book

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import sys
import string
import random

# Markov class, encapsulating most of the functions from the original
# markov module. Remember to add an initial argument (self) to each of the
# methods to represent the object being asked to call the method.
class Markov:

    def __init__(self):
        # No longer global variables, now class attributes
        self.suffix_map={}  # map from prefixes to a list of suffixes
        self.prefix = () # current tuple of words
        
    def process_word(self, word, order=2):
        """Processes each word.

        word: string
        order: integer

        During the first few iterations, all we do is store up the words; 
        after that we start adding entries to the dictionary.
        """
        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]
            
            self.prefix = shift(self.prefix, word)

    def process_file(self, filename, order=2):
        """Reads a file and performs Markov analysis.

        filename: string
        order: integer number of words in the prefix

        returns: map from prefix to list of possible suffixes.
        """
        fp = open(filename)
        skip_gutenberg_header(fp)

        for line in fp:
            if line.startswith('*** END OF THIS'): 
                break

            for word in line.rstrip().split():
                self.process_word(word, order)
                
    def random_text(self, n=100):
         """Generates random wordsfrom the analyzed text.

         Starts with a random prefix from the dictionary.

         n: number of words to generate
         """
         # choose a random prefix (not weighted by frequency)
         start = random.choice(list(self.suffix_map.keys()))

         for i in range(n):
             suffixes = self.suffix_map.get(start, None)
             if suffixes == None:
                 # if the start isn't in map, we got to the end of the
                 # original text, so we have to start again.
                 self.random_text(n-i)
                 return

             # choose a random suffix
             word = random.choice(suffixes)
             print(word, end=' ')
             start = shift(start, word)
                
# Leaving these as global functions, because it doesn't
# seem to make sense to have it associated with a particular
# set of text. Could also just use it as a class method
# of Markov.
# Basically they seem more generic, and not directly related
# to a specific text, or even this specific task. 
def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)



def main(script, filename='../chap13/kafka.txt', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else:
        book_markov = Markov()
        book_markov.process_file(filename, order)
        book_markov.random_text(n)
        print()


if __name__ == '__main__':
    main(*sys.argv)
