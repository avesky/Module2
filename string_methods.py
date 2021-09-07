"""
Program: string_methods.py
Author: Andy Volesky
Last date modified: 09/06/2021

The purpose of this program: Test a variety of string methods and print result.
"""

test_string = "neo in the matrix"

#capitalize
cap = test_string.capitalize()
print(cap)

#find
found = test_string.find('matrix')
print(found)

#index
i = test_string.index('in')
print(i)

#isalnum
is_num = test_string.isalnum()
print(is_num)

#isalpha
is_alpha = test_string.isalpha()
print(is_alpha)

#isdigit
is_dig = test_string.isdigit()
print(is_dig)

#islower
is_lower = test_string.islower()
print(is_lower)

#isupper
is_upper = test_string.isupper()
print(is_upper)

#isspace
is_space = test_string.isspace()
print(is_space)

#startswith
starts = test_string.startswith('neo')
print(starts)