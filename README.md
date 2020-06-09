Think Python
====

Exercises in the Think Python 2nd Edition, by Allen B. Downey.

#### Chapter 2
[Exercises](chap2/chap2.py)

#### Chapter 3
[Exercises](chap3/chap3.py)

More robust version of [3.3](chap3/chap3_alt.py)

#### Chapter 4
Section 4.3 [Exercises](chap4/mypolygon.py)

Exercises in section 4.12
* 4.1, stack diagram is an important concept
* 4.3, polygon pies, is relatively straightforward. Might be good to know about 'math.sin(x)', which is in the math.py package. You can use it by having the line `import math` at the top of your python module. Note that the pie slices are isosceles triangles, which can be split up into two right triangles.
* 2,4 and 5 are a little trickier (or more involved, in the case of 4). Could probably be skipped.

[Exercises 4.1-4.5](chap4/chap4.py)

#### Chapter 5
These exercises all seem good and straightforward. The last one (5.6.3) could be tricky to figure out depending on which fractal you pick.
Also for 5.1, the book doesn't necessarily make it clear that the number returned by time.time() is the number of seconds since midnight on the given start date of the epoch.

Exercises: [5.1](chap5/epoch.py), [5.2](chap5/fermat.py), [5.3](chap5/triangle.py), [5.4](chap5/recurse.py), [5.6](chap5/koch.py)

#### Chapter 6
[Exercises](chap6)

#### Chapter 7
I wouldn't worry too much about the table of square roots looking pristine, as there are more (better) ways of formatting for the future. But it can still be interesting to make it look nice, and the key (with tools so far described) is using str(n) to cast a number to a string, so you can use len() on it (e.g. `len(str(5.31))=4)`. And also concatenate it with other strings. Also helpful to note that by default, Python seems to display a max of 16 digits after the decimal place (so 18 characters total for positive numbers less than 10).

[Exercises](chap7)

#### Chapter 8

Section 8.3 [Exercises](chap8/practice.py)

Exercises [8.2-8.4](chap8/string_methods.py), [8.5](chap8/caesar.py)

#### Chapter 9
It starts to become useful around here to make multiple files and be able to import functions from your own modules. If all the modules (.py files) are in the same directory, this can be done just like importing the math module, with `import <modulename>`. E.g. if a file name is wordlist.py, you can access all the functions in that file by using `import wordlist` at the top of your new module.

Exercises [9.1-9.6](chap9/words.py), [9.7](chap9/cartalk.py), [9.8](chap9/odometer.py), [9.9](chap9/ages.py)

#### Chapter 10
[Exercises 10.1-10.7](chap10/lists.py), [10.8](chap10/birthdays.py), [10.9](chap10/wordlist.py), [10.10](chap10/inlist.py),
[10.11](chap10/reverse_pair.py), [10.12](chap10/interlock.py)
There's also a [testing module](chap10/test.py) for the first 7 exercises.

#### Chapter 11
For exercise 11.3, the memoization of the Ackerman function, it'll be useful to look up tuples, which the chapter briefly mentions. Tuples are immutable lists, which means you can hash them and use them as keys in a dictionary. So something like `known[(m,n)]` for accessing/storing `ack(m,n)`.

Exercise [11.1](chap11/worddict.py), [11.2](chap11/inver_dict.py), [11.3](chap11/ackermann_memo.py), [11.4](chap11/has_duplicates.py), [11.5](chap11/rotate_pairs.py), 11.6 [pronuncation data reader](chap11/pronounce.py) and [homophone finder](chap11/homophone.py)

#### Chapter 12
[Practice exercises](chap12/practice.py)

Exercise [12.1](chap12/most_frequent.py), [12.2](chap12/anagram_sets.py), [12.3](chap12/metathesis.py), [12.4](chap12/reducible.py)

#### Chapter 13
Exercises [13.1-13.7](chap13/analyze_book.py), [13.8](chap13/markov.py), [13.9](chap13/zipf.py)
