Think Python
====

Exercises in the Think Python 2nd Edition, by Allen B. Downey.

#### Chapter 4
Exercises in section 4.12
* 4.1, stack diagram is an important concept
* 4.3, polygon pies, is relatively straightforward. Might be good to know about 'math.sin(x)', which is in the math.py package. You can use it by having the line `import math` at the top of your python module. Note that the pie slices are isosceles triangles, which can be split up into two right triangles.
* 2,4 and 5 are a little trickier (or more involved, in the case of 4). Could probably be skipped.

#### Chapter 5
These exercises all seem good and straightforward. The last one (5.6.3) could be tricky to figure out depending on which fractal you pick.
Also for 5.1, the book doesn't necessarily make it clear that the number returned by time.time() is the number of seconds since midnight on the given start date of the epoch.

#### Chapter 7
I wouldn't worry too much about the table of square roots looking pristine, as there are more (better) ways of formatting for the future. But it can still be interesting to make it look nice, and the key (with tools so far described) is using str(n) to cast a number to a string, so you can use len() on it (e.g. `len(str(5.31))=4)`. And also concatenate it with other strings. Also helpful to note that by default, Python seems to display a max of 16 digits after the decimal place (so 18 characters total for positive numbers less than 10).

#### Chapter 9
It starts to become useful around here to make multiple files and be able to import functions from your own modules. If all the modules (.py files) are in the same directory, this can be done just like importing the math module, with `import <modulename>`. E.g. if a file name is wordlist.py, you can access all the functions in that file by using `import wordlist` at the top of your new module.
