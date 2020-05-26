# Exercise 6.3 Palindromes

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# 6.3.1
print(middle('ab')) #blank
print(middle('a'))  #blank
print(middle(''))   #blank

# 6.3.2
def is_palindrome(word):
    mid_word = middle(word)
    # Base case, even if there is one middle character there's no need to check it
    # Incidentally, if there is just one (odd length word) we'll never see it on
    # its own, since middle('a')=''.
    if mid_word=='':
        return True
    return first(word)==last(word) and is_palindrome(mid_word)

# Test is_palindrome
print("Is it a palindrome?")
print("Test", is_palindrome("test"))
print("abba", is_palindrome("abba"))
print("redivider", is_palindrome("redivider"))
