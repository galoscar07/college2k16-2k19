'''
Created on Oct 16, 2016

@author: Arthur
'''

'''
    NB!
    Uncomment each of the sections separated by ### below,
    one at a time and run them
'''

'''
We first try to run the functions in the fibo module without import
'''
#print(fibTerm(5))

#############################

'''
This enters the fibo module's name into the symbol table
    Which of the function calls below is correct?
'''

# import fibo
# print(fibTerm(5))
# print(fibo.fibTerm(5))

#############################

'''
If there is no name conflict, we can import function names directly
    What is the cause of the error in the code below?
'''

# from fibo import fibTerm
# print(fibTerm(5))
# print(fibSequence(5))

#############################

'''
Using *, we can import all names from a module
'''
# from fibo import *
# print(fibTerm(5))
# print(fibSequence(5))

#############################

'''
What happens if we have the same function names in 2 modules?
    Hint - Try switching the order of the import's below
    
    NB! This is VERY bad design, as you don't know what is actually called 
'''

# from fibo import *
# from fiboDummy import *
# print(fibTerm(5))

#############################

'''
Here is the correct example for same-name functions

This way you have control on what is called
'''
# import fibo
# import fiboDummy
# print(fibo.fibTerm(5))
# print(fiboDummy.fibTerm(5))

#############################

'''
Last but not least, you can examine what a module/function does using the 'help' function
'''
import fibo
import fiboDummy

help(fibo)
help(fibo.fibTerm)










