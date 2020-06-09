# Function call examples

def print_spam():
    """Just prints the word spam.
    """
    print("spam")

# This function takes in one argument, f.
# The argument as listed here must be a symbol, a valid
# variable or function name.
# def do_twice(f):
# def do_twice(any_letters_and_underscores_and_numb3rs):
# The following don't work:
# def do_twice(3_things): <-- symbols can't start with a number
# def do_twice(f()): <-- symobls can't contain parentheses
# With that last one, since the entire symbol in the argument is
# f(), it thinks you're trying to use f() as a symbol. But () can't be
# part of a symbol.

def do_twice(f):
    """Calls the function f twice, no arguments
    """
    f()
    f()

# The argument is shorthand for "set this symbol equal to the input
# we get." So when you call do_twice(print_spam), python goes to
# the definition of do_twice and sees 'f' there as the argument.
# Then it does this:
# f = print_spam
# Then it runs the statements in do_twice, which are f() and f().
print("**do_twice(print_spam) result:")
do_twice(print_spam)

# To see the return value of do_twice(print_spam), you can
# assign it to a variable. In this case, the return value should
# be None
print("**do_twice(print_spam) result, again:")
do_twice_result = do_twice(print_spam)
print("**do_twice(print_spam) return value is", do_twice_result)

# Similarly, the return value of print_spam() is None.
# So if you call do_twice(print_spam()), now instead of
# passing print_spam, which is a function object, you're
# passing the return value of print_spam(), which is None
# So the function would do this:
# f = None
# Then it tries to do f()->None(), but None is not a function
# so it can't be called with ().
# do_twice(print_spam()) # <-- Error


# Functions can have return values that are not None.
def always_returns_5():
    """This function always returns 5. Does nothing else.
    """
    return 5

# Now call always_returns_5 and store its return value
print("**Calling always_returns_5()")
always_returns_5_result = always_returns_5()
print("**Return value of always_returns_5():", always_returns_5_result)
print("**Now call do_twice(always_returns_5).")
dt_always_returns_5_result = do_twice(always_returns_5)
print("**Return value of do_twice(always_returns_5):", dt_always_returns_5_result)
# Notice that do_twice still returns None, because it has no return
# value. always_returns_5() was called twice in do_twice, but we
# didn't assign it to anything or print it, so it had no effect.

# Now for a case where we can pass a function call.
def return_print_spam():
    """This function returns the function object print_spam
    """
    return print_spam

# Just to see what this function does..
print("**Calling return_print_spam() and assigning it to a variable.")
return_print_spam_result = return_print_spam()
print("**Return value of return_print_spam() is", return_print_spam_result)
print("**This should be the same as the print_spam function value.")
print("**Just to check that, print_spam value is", print_spam)

# Now we can do this:
print("**Calling do_twice(return_print_spam())")
do_twice(return_print_spam())
# do_twice will again take whatever is in the argument spot
# and assign it to f. 
# But as we just saw, return_print_spam() is print_spam
# So f-->return_print_spam()-->print_spam
# So in do_twice, f() is the same as print_spam()
