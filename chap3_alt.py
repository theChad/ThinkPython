# Slightly altered implementation of box problem
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
    
# Print full top/bottom row of boxes
# Input function do_times will be responsible for repeating the pattern
# E.g. make do_times = do_twice to print the top/bottom of two boxes
def top_boxes(do_times):
    do_times(top_box_segment)
    top_box_final()
    
# Print one segment of the middle of one box (|         )
def mid_box_segment():
    print('|'+' '*9, end='')

# Print the final segment of the middle of a box (|)
def mid_box_final():
    print('|')

    # Print a full middle row of 2 boxes
# Agin input function do_times will repeat the pattern some number of times
def mid_boxes(do_times):
    do_times(mid_box_segment)
    mid_box_final()
    
# Print several boxes side-by-side (no bottom layer)
# do_times is a function responsible for repeating the box a certain number of times
def make_boxes(do_times):
    top_boxes(do_times) #top row
    # This next bit a is a little tricky. We want a function that we can pass
    # to do_four to create our four rows of middle lines. Right now that depends
    # on the number of boxes in the row, i.e. on what do_times is. This new
    # function, mid_xboxes_times, will *use* do_times inside of it, so it will
    # no longer have to be fed do_times separately.
    # Note that mid_boxes_times is internal to this function (make_boxes).
    # If we tried to call mid_boxes_times outside of make_boxes, python would
    # throw an error because it's out of scope.
    def mid_boxes_times():
        mid_boxes(do_times)
    do_four(mid_boxes_times) #four middle rows

# Print nxn boxes
def make_box_nxn(do_times):
    # Similar to mid_boxes_times in make_boxes, we want a function with no argument
    # that we can call with do_twice or do_four
    def make_boxes_times():
        make_boxes(do_times)
    do_times(make_boxes_times) #nxn boxes(no bottom layer)
    top_boxes(do_times) #bottom layer

# Now all we have to do to print out nxn boxes is pass, to make_box_nxn, a function
# that calls its argument function n times.
    
# Actually print out the boxes
print("3.3.1 2x2 boxes test")
make_box_nxn(do_twice)

# 3.3.2
#-------------------------
# Test out the 4x4
print("3.3.2 4x4 boxes test")
make_box_nxn(do_four)

# Just for fun an 8x8
def do_eight(f):
    do_four(f)
    do_four(f)
print("8x8 boxes test")
make_box_nxn(do_eight)
