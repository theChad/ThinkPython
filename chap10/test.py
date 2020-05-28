# Testing module for chapter 10 problems

import lists
from ..chap9 import words

def test_lists():
    nested_lists = [[[1,2],[3],[4,5,6]],
                    [[[2,[3],[4,5],6],7]],
                    [1.25, [2.75, [3.50]] ,2.5],
                    []]
    flat_lists = [[1,2,3,4,5,6],
                  [6,5,4,3,2,1],
                  [5,6,3,2,4,5,6,7,8,9,4,3,10,23,156],
                  [66,23,643,432,7654,234,12,23,7654],
                  [23,56,64,83,74,52,53,88],
                  [1,2,3],
                  [2,3],
                  [23],
                  []]
    strings = ['This is a test',
               'This is not a test',
               'binary',
               'adobe',
               'listen',
               'anagram',
               '']
    strings_2 = ['This is not a test',
                 'This is a test',
                 'brainy',
                 'abode',
                 'silent',
                 'nagaram',
                 '']
    # nested_sum test
    for l in nested_lists:
        print('---------------------------------------')
        print(l)
        print('---------------------------------------')
        print("Sum:",lists.nested_sum(l))
    # flat list tests
    for l in flat_lists:
        print('---------------------------------------')
        print(l)
        print('---------------------------------------')
        print("Cumulative sum:", lists.cumsum(l))
        print("Middle:", lists.middle(l))
        print("Is_sorted:", lists.is_sorted(l))
        print("Has_duplicates:", lists.has_duplicates(l))
        lists.chop(l) # modifies the list
        print("Chop:", l)
    # anagram
    for s,t in zip(strings, strings_2):
        print(s,"and",t,"are anagrams. <-", lists.is_anagram(s,t))
        
test_lists()
