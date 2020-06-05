import analyze_book, math

# Exercise 13.9

def print_logs(filename="book.txt"):
    """Print the relevant logarithms from Zipf's law,
    log(frequency) and log(rank) - rank is the order of most
    frequent words
    """
    word_hist = analyze_book.get_only_words(filename)
    freq_words = analyze_book.invert_dict(word_hist)
    freqs = sorted(freq_words.keys(), reverse=True)
    r=0
    for i in range(100):
        # I have a reverse histogram dictionary, so each entry
        # could have multiple words (per frequency). Run through
        # all of them and adjust rank accordinly.
        for j in range(len(freq_words[freqs[i]])):
            r += 1
            print(math.log(freqs[i]),math.log(r),sep='\t')
    
if __name__=='__main__':
    print_logs('double.txt')
