from typing import List
import time
import gc
# Here in this code we will be leaking memory because we are creating cyclic reference. 
# Find that we are indeed making cyclic references.
# Eventually memory will be released, but that is currently not happening immediately.
# We have added a function called "clear_memory" but it is not able to do it's job. Fix it. 
# Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that
# this code is sub-optimal.
class Something(object):

    def __init__(self):
        super().__init__()
        self.something_new = None

    def __repr__(self):
        return f'This is object of type {type(self)} at address {id(self)}'

class SomethingNew(object):

    def __init__(self, i: int = 0, something: Something = None):
        super().__init__()
        self.i = i
        self.something = something

    def __repr__(self):
        return f'This is object of type {type(self)} at address {id(self)}'

def add_something(collection: List[Something], i: int):
    something = Something()
    something.something_new = SomethingNew(i, something)
    collection.append(something)

def reserved_function():
    # to be used in future if required
    pass

def clear_memory(collection: List[Something]):
#    for obj in collection:
#        obj.something_new.something=None        
    collection.clear()
    gc.collect()


def critical_function():
    collection = list()
    for i in range(1, 1024 * 128):
        add_something(collection, i)
    clear_memory(collection)


# Here we are suboptimally testing whether two strings are exactly same or not
# After that we are trying to see if we have a particular character in that string or not
# Currently the code is suboptimal. Write it in such a way that it takes 1/10 the current time

# DO NOT CHANGE THIS PROGRAM
def compare_strings_old(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass

# YOU NEED TO CHANGE THIS PROGRAM
def compare_strings_new(n):
    import sys
    a = sys.intern('a long string that is not intered' * 200)
    b = sys.intern('a long string that is not intered' * 200)
    string_match=0
    for i in range(n):
        if a is b:
            string_match=1

    if string_match == 1:
        print('Both String are same!')
    else:
        print('Both String are not Same!') 

    char_list = set(a)
    membrship_test = 0
    for i in range(n):
        if 'd' in char_list:
            membrship_test = 1

    if membrship_test == 1:
        print('Membership Test Passed!')
    else:
        print('Memebership Test Faile!') 