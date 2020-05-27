# Exercise 10.9

# list_plus is way longer. Append updates the list object,
# but the + operator creates a whole new list each time,
# which we then assign back to words.


# To see how long they take I have them both return null so it doesn't print out
# the whole list. Could also just do an assignement in the shell to avoid that.
# E.g. a=list_append()
def list_append(filename="../chap9/words.txt"):
    words=[]
    fin = open(filename)
    for line in fin:
        word = line.strip()
        words.append(word)
    return words

def list_plus(filename="../chap9/words.txt"):
    words=[]
    fin = open(filename)
    for line in fin:
        word = line.strip()
        words = words + [word]
    return words
