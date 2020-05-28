# Exercise 8.5

def rotate_char(c, n):
    """Rotate a single character n places in the alphabet
    n is an integer
    """
    # alpha_number and new_alpha_number will represent the
    # place in the alphabet (as distinct from the ASCII code)
    # So alpha_number('a')==0

    # alpha_base is the ASCII code for the first letter of the
    # alphabet (different for upper and lower case)
    if c.islower():
        alpha_base = ord('a')
    elif c.isupper():
        alpha_base = ord('A')
    else:
        # Don't rotate character if it's not a letter
        return c

    # Position in alphabet, starting with a=0
    alpha_number = ord(c) - alpha_base
    
    # New position in alphabet after shifting
    # The % 26 at the end is for modulo 26, so if we shift it
    # past z (or a to the left) it'll wrap around
    new_alpha_number = (alpha_number + n) % 26

    # Add the new position in the alphabet to the base ASCII code for
    # 'a' or 'A' to get the new ASCII code, and use chr() to convert
    # that code back to a letter
    return chr(alpha_base + new_alpha_number)


def rotate_word(s, n):
    """Rotate each character in s, n places in the alphabet.
    e.g. rotate('ab',2) returns 'cd'
    s: string
    n: integer to shift (cast to integer in case float is received)
    """
    n=int(n) # Make sure n is integer
    # We'll build up the encoded version letter by letter, so
    # start with the empty string
    s_rot = ''
    for c in s:
        # ord(c) gives us the ASCII code for the character c
        # Adding n to that number gives the 
        s_rot += rotate_char(c, n)
    return s_rot


