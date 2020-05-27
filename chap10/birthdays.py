# Exercise 10.8
import random
import lists

def random_birthday():
    """Generate a random birthday by numbered day of the year.
    """
    # Ignore the fact that leap birthdays are less likely and just use 366
    return random.randint(1,366)


def share_birthday(num=23, iterations=1000):
    """What is the probability the num people share the same birthday?
    iterations: Number of samples of num students to generate
    """
    counter = 0
    for i in range(iterations):
        # Generate birthdays
        birthdays = []
        for j in range(num):
            birthdays.append(random_birthday())
        if lists.has_duplicates(birthdays):
            counter += 1
    return counter/iterations

print("Probability:",share_birthday())
