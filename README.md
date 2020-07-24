# Session 2- Object Mutability and Interning Assignment

This assignment project is written in Python, and tested with pytest. It includes following files.
-session2.py      : This is the assignment code which needs to be fixed
-test_session2.py : This is pytest unit test. It tests completeness of assignment

>This assignment checks understanding of following concepts:
- Memory leaks due to cyclic reference
- Performance of string comparison using elementwise comparison and using referenced object compariosn
- Performance of membership test in list and set
- Getting familiar with Markdown language (md) to write a good quality README file

> Description of Functions/Class along with bug fixes

### Something
This is a class object. It accepts object as arguement. But this arguement is not used anywhere.
It has a attribute reference "something_new". something_new has binding to None object. 

### SomethingNew
This is a class object. Its inittialization function expects integer object and instance of class Something as arguement.
It has two attribute reference: i and something. 
Attribute reference i stores integer value.
Attribute reference something creates binding to instace of class Something passed arguement. This implementation may create cyclic reference if not used carefully.
Function add_something exploits this implementation to create memory leak.

### add_something
This is a function object. It expects List object and integer object as arguement.
When called this function appends an instace of class something in the List object.
But it creates cyclic reference by making attribute something_new of class Something to reference object of class SomethingNew. 
As attribute something of class SomethingNew references to object of class Something passed as arguement it creates cyclic reference.   

-First it creates object something of class Something.

`something = Something()`

-Then it passes object something to create object of class SomethingNew and this object of class something_new is referenced by attribute reference something_new.

`something.something_new = SomethingNew(i, something)`

- In class SomethingNew the attribute something references object passed as arguement which creates cyclic reference.

`self.something = something`

- Now attribute something_new of class something has reference of class SomethingNew and attribute something of SomethingNew has reference of class something!

### clear_memory
This is a function object. It expects list object as arguement.
It frees the memory occupied by the list object. It uses clear() method of list class. Clear method removes all elements of class.
All the elements appended by function add_something are object of class something. Clear method removes reference by list to this objects.
But add_something function has created cyclic reference between class something and SomethingNew all objects still exists in memory.
This memory can be freed by calling garbage collector manualy.

`   collection.clear()
    gc.collect()`

Or alternatively 
	
This can be removed by this cyclic reference by repointing attribute something of class SomethingNew to None object before clearing list:

`     for obj in collection:
        obj.something_new.something=None
	  collection.clear()`

### critical_function
This is a function object. This function appends 1024*128 elements in list "collection" by calling function add_something.
After creating list it frees memory by calling function clear_memory. 

### compare_strings_old
This is a function object. It expects integer object (n) as arguement. It first	performs element wise compariosn between two strings of size of 43*200. It repeats this action n time.  
It also performs membership test of charactor 'd' in one of the string which is stored as a list. Membership test in list is a very slow process.
Here the method used for string compariosn and membership test are very inefficient methods.

### compare_strings_new
This a function object. This function is improved implementation of compare_strings_old in terms of performance.
In this function we are forcing python to store a long noninterning string as a interned string using sys.intern() command.
As string is interned, any other assignment of same string will create reference to same memory location. 
So now if two string are same or not that can be verified by validating if both object are same or not.

In compare_strings_old the string comparison implementation is incomplete. It doesn't say the result of string comparison. I have updated this.
If for a noninterning string, string comparison is performed by checking if both object are same or not the comparison will fail even if the string are same.
But execution of comparison will be faster than element wise comparison.

### sleep
The sleep() function suspends (waits) execution of the current thread for a given number of seconds.

### char_list
In object char_list string is stored as characters. If  string is stored as list membershipt test will be slow. If string is stored as set the membership test is fast.

### collection
Collection is list object. 

### __init__
When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance.

### Unit Test Results

Unit test results screenshot uploaded in Unit_Test_Results.JPG