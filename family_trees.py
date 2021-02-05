# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.
# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }





person = str(input("Give name? "))

value_list=genealogy[person]
print(value_list)



#def ancestors(genealogy,person):
#   for x, y in genealogy.items():
#   #x=key
#     #y=value
#    if (x==person):
#         print(y)
#         return y