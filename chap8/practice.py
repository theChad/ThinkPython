# Section 8.3 exercises

def print_rev_string(s):
    """Prints s in reverse, one letter per line
    """
    # Index variable i will start at -1, since s[-1] is the last letter of s
    i = -1
    # Print s[i], going backwards through the string by decreasing i
    # every time. s[-len(s)] will be the first letter.
    while i >= -len(s):
        print(s[i])
        i-=1 # decrement i to get to next lett from the end


print_rev_string('this is a test')

# Make Way for Ducklings modification
def make_way():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        # Instead of Q, we want to use Qu. So check letter each time.
        # Do nothing unless letter is Q, in which case change it to Qu.
        if letter=='Q':
            # This will concatenate u onto letter, making it Qu.
            # The same as saying letter = 'Qu', since we are already guaranteed
            # that letter starts as Q here.
            letter += 'u'
        print(letter + suffix)

make_way()

# Section 8.6 exercise

# Make index a parameter of the function (defaulted to zero).
# No need to set index to zero in the code now, and the rest of the
# code remains unchanged. If index>0, it's as if we've already looked through
# the first <index> characters and didn't find <letter> yet.

def find(word, letter, index=0):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, letter):
    count = 0
    index = 0
    # Keep calling find until it can't find a letter
    while True:
        # Save the index of the next occurence of letter
        index = find(word, letter, index)
        # find returns -1 if it couldn't find the letter
        # So if index is -1, we've reached the end of the word with no
        # more occurences of letter. Break out of the loop.
        if index==-1:
            break

        # If index is any other number, find() found another occurence of
        # letter, so increment the count
        count += 1
        # Increment index also, so find() won't just keep finding the
        # same occurence of the letter. We need to start looking on the letter
        # after the one we just found
        index += 1
        
    print(count)

count("this is a test",'t')

# Section 8.11

# The error is in the while condition, while j > 0. Since indices start
# at zero, we'll always miss the first letter of the word and won't check
# it against the last letter of the other word.


