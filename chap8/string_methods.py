# Exercise 8.2

# You can call a method directly on the string, as well as on a variable
# of type string. So here I call count directly on 'banana', with the
# argument 'a' as the letter/substring to count.
print('banana'.count('a'))

# Exercise 8.3

def is_palindrome(s):
    # The slice uses the entire string if the start and end are left out.
    # So s[::1]==s[0:len(s):1]. And s[::-1] knows you're moving backwards
    # (since the last argument to the slice is negative), so it automatically
    # starts at the last (rightmost) element of the string.

    # Since s[::-1] is the reverse of s, we just have to see if it's equal
    # to s. If it is, then s is a palindrome. So we can just return the
    # result of that comparison directly
    return s==s[::-1]

# Exercise 8.4
# (Possibly) incorrect functions

# This function checks to see if the *first* letter in a string is lowercase.
# If the first letter is uppercase, it exits the function with
# return False
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        # Since we have an else clause, we're guaranteed to do either
        # the body of the if statement or the body of the else statment.
        # Which means this function will be returning (and thus exiting)
        # after the first letter, no matter what.
        else:
            return False

# This time it returns a string
# that reads "True" or "False", instead of a boolean. So if you wanted
# to use it in other code it would probably be useless, since Python
# treats nonempty strings as True. Basically this function returns True
# no matter what.
# False is False, but 'False' is True.
# if('False'): do thing  <-- would do the thing
# if(False): do thing    <-- would not do the thing
# The other problem is instead of checking characters in the string, it
# just checks the character 'c', which of course is lower case.
# So it will actually never return 'False', and always return 'True'.

def any_lowercase2(s):
    for c in s:
        if 'c'.islower(): # Should be if c.islower():, no quote
            return 'True'
        else:
            return 'False'

# Getting closer, but now it just tells us whether the *last* character
# in the string is lowercase. Since it doesn't combine new knowledge with any
# previous information, it just sets the flag anew with each character it reads
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# This one works! It initializes the flag to false, since we haven't found
# any lowercase letters yet. Then it uses or, which returns true if
# either of the arguments is true. So once we find a lower case letter,
# flag will stay true for the rest of the program.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# This one determines whether *all* letters are lowercase. The first time
# it encounters a non-lowercase letter, it stops and returns False.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# A more efficient version of any_lowercase4, inspired by anylowercase_5.
# For something like a counter, we need to run
# through the whole list. For this, as soon as we find the first lowercase
# letter we're done, because we know there's at least one. So we can return True
# and stop execution of the function as soon as the first lowercase letter
# pops up.

def any_lowercase6(s):
    for c in s:
        if c.islower():
            return True
    return False
