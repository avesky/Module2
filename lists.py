"""
Program: lists.py
Author: Andy Volesky
Last date modified: 09/06/2021

The purpose of this program: Test a variety of list methods and print result.
"""

list_one = ['Janet', 'Reno', 'Dance Party']
print(list_one)

#append - add another string.
list_one.append('So Dance!')
print(list_one)

#copy - (you need two string variables) copy list_one to list_two and print both
list_two = list_one.copy()
print(list_one)
print(list_two)

#index - retreive an item at a index, and see what happens for an index that does not exisit in the list
i = list_one.index('Reno')
print(i)
#i_two = list_one.index('Wizard Party') get error 'Wizard Party not in the list
#print(i_two)

#count
count = list_one.count('Janet')
print(count)

#insert
list_one.insert(2,'This is my')
print(list_one)
list_one.insert(0, "My name is")
print(list_one)

#remove
list_one.remove("Reno")
print(list_one)

#reverse
list_one.reverse()
print(list_one)

#sort
list_one.sort()
print(list_one)

#clear
list_one.clear()
print(list_one)