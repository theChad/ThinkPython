# 3.1
#-------------------------
def right_justify(s):
    print(" "*(70-len(s))+s)

print("Testing right_justify:")
right_justify("test")
right_justify("This is just another test.")


#3.2.1
#-------------------------
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
print("3.2.1")
do_twice(print_spam)
#3.2.2
def do_twice(f,v):
    f(v)
    f(v)
# 3.2.3
def print_twice(bruce):
    print(bruce)
    print(bruce)
# 3.2.4
print("3.2.4")
do_twice(print_twice,'spam')
# 3.2.5
def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)
print("3.2.5")
do_four(print,'spam')

# 3.3.1
#-------------------------
# Rewrite the the do twice and do four functions for just one input
def do_twice(f):
    f()
    f()
def do_four(f):
    do_twice(f)
    do_twice(f)

# Print one segment of the top/bottom of a box (+ - - - -)
def top_box_segment():
    print('+', '- '*4, end='')
# The final character of the top of a box (+)
def top_box_final():
    print('+')
# Print full top/bottom row of a 2 boxes
def top_box_2():
    do_twice(top_box_segment)
    top_box_final()
# Print one segment of the middle of one box (|         )
def mid_box_segment():
    print('|'+' '*9, end='')
# Print the final segment of the middle of a box (|)
def mid_box_final():
    print('|')
# Print a full middle row of 2 boxes
def mid_box_2():
    do_twice(mid_box_segment)
    mid_box_final()
# Print 2 boxes side-by-side (no bottom layer)
def make_box_2():
    top_box_2() #top row
    do_four(mid_box_2) #four middle rows
# Print 2x2 boxes
def make_box_2x2():
    do_twice(make_box_2) #2x2 boxes(no bottom layer)
    top_box_2() #bottom layer

# Actually print out the boxes
print("3.3.1 2x2 boxes test")
make_box_2x2()

# 3.3.2
#-------------------------
# Top/bottom layer of 4 side-by-side boxes
def top_box_4():
    do_four(top_box_segment)
    top_box_final()
# Mid layer 4 side-by-side boxes
def mid_box_4():
    do_four(mid_box_segment)
    mid_box_final()
# Print 4 boxes side-by-side (no bottom layer)
def make_box_4():
    top_box_4() #top row
    do_four(mid_box_4) #middle rows
# Print 4x4 boxes
def make_box_4x4():
    do_four(make_box_4) #4x4 boxes (no bottom layer)
    top_box_4() #bottom layer
# Test out the 4x4
print("3.3.2 4x4 boxes test")
make_box_4x4()
