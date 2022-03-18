'''

In Python lambda functions are:
1. anonymous or nameless functions
2. 'lambda' is not a name, but its a keyword
3. They are also called throwaway function

Why are they used:
1. One time use - also knows as thrown away functions as they are needed just once
2. I/O of other functions - They are also passed as inputs or returned as outputs of other functions 
3. Reduce code size - The body of a lambda function is written in single line

A lambda function is created using lambda operator

SYNTAX:
lambda arguments: expression

'''

x = lambda a: a * a
x(3)
