# Deep Count
from typing import Iterable

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.
# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.
# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:


#len() function returns the number of items in an object, when object is a string returns the number of characters in the string
#procedure in python
#Functions differ from procedures in that functions return values, unlike procedures which do not. However, parameters can be passed to both procedures and functions.

#Question 1: Difference between procedure and function: The first does not return anything the second does?(A procedure performs a task, whereas a function produces information.
# Functions differ from procedures in that functions return values, unlike procedures which do not.
# However, parameters can be passed to both procedures and functions.
#Question 2: If an element has another list inside do I need to make a loop with i,j,k?
#Question 3: How do I check if an element/value is a list?
#How do I use len function in this exercise?
#The yield statement suspends function's execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off.
# When resumed, the function continues execution immediately after the last yield r

today = [['WESTMINSTER', 500, 8000], [[1, 2, 3], 150, 16000], ['UCL', 190, 40000], ['Manchester',50,3000]]



# def flatten(lis):
#     for item in lis:
#         print(str(item) + "\n")
#         if isinstance(item, Iterable) and not isinstance(item, str):
#             for x in flatten(item):
#                 yield x
#         else:
#             yield item



def deep_count_Olga(today):
    count = 0
    for sum in range(len(today)):

        for j in range(len(today[sum])):
            count += 1
    print('Total Count of elements in this list is', count)



    # return count


def is_list(p):
    return isinstance(p, list)

#correct solution
def deep_count_Dimitris(p):
    cnt = 0
    for e in p:
        cnt += 1
        if is_list(e):
            cnt += deep_count_Dimitris(e)
    return cnt

deep_count_Olga(today)
# print(str(flatten(today)))
#if I have a list embedded in a list embedded in another list
