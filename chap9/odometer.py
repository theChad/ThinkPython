# Exercise 9.8
# Odometer started at 198888

def has_palindrome(word, start, end):
    """Determine if a word has a palindrome from the position start to 
    the position end, exclusive of end like normal slice
    start: start of questioned palindrome
    end: end of questioned palindrome
    """
    # Find the reverse of the portion of the word. Special case for starting at the beginning
    # of the word
    if start==0:
        reverse_word = word[end-1::-1]
    else:
        reverse_word = word[end-1:start-1:-1]
    # That portion is palindromic if it's equal to its reverse
    return word[start:end]==reverse_word

def padded_num_to_str(num, characters):
    """Return a string of the number, left-padded with zeros up to characters
    num: number to convert
    characters: number of total characters in resultant string, zero-padded
    """
    word = str(num)
    padded_word = (characters-len(word))*'0' + word
    return padded_word

def consecutive_palindromes():
    """Find 4 consecutive 6-digit numbers with palindromes in them as follows:
    Last 4 palindromic
    Last 5 palindromic
    Mid  4 palindromic
    All  6 palindromic
    """
    count = 0
    i = 0
    # Cycle from 0 to 999,999
    while i < 1000000:
        # Get a string version of the number showing all digits the odometer would show
        word = padded_num_to_str(i, 6)
        # Set a flag to keep track of whether we found the next palindrome in the
        # sequence this go around.
        palindrome_flag = False
        if count == 0:
            # Last four palindrome
            # Increment the palindrome sequence count, move onto next number
            if has_palindrome(word,2,6):
                count += 1
                i += 1
                palindrome_flag = True
        # If we already found exactly one palindrome this sequence, onto the next one
        elif count == 1:
            # Last 5 palindrome
            if has_palindrome(word,1,6):
                count += 1
                i += 1
                palindrome_flag = True
        elif count == 2:
            # Mid 4 palindrome
            if has_palindrome(word,1,5):
                count += 1
                i += 1
                palindrome_flag = True
        elif count == 3:
            # All 6 palindrome
            if has_palindrome(word,0,6):
                # Found them all! Return the first palindrome in the sequence.
                return i-3
        # If we didn't find the appropriate palindrome in the sequence, reset the count
        # and go back to the number after the first palindrome we found in this
        # sequence
        if not palindrome_flag:
            i += 1 - count
            count = 0
        
        
    print("didn't find it.")
    return 

#print(consecutive_palindromes())
