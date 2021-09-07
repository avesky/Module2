"""
Program: average_scores.py
Author: Andy Volesky
Last date modified: 09/06/2021

The purpose of this program:

Prompt the user for what is expected for each input
Store into local variables last_name, first_name.
Use a constant to represent the number of scores you will prompt the user to input
Prompt the user for the scores, storing them in local variable or variables.
You can keep separate variables for each score, or you keep a running total in one variable.
Calcuate the average using the variables.
Print the output, with last name followed by a comma and the first name followed by an integer age and then the average scores with 2 decimal places.
Example output:
Rodriguez, Linda age: 21 average grade: 92.50
Add doctring to the top of your file, add comments at the bottom with observed output after a few manual test runs of your code..
"""
from constants import NUM_SCORES

#asking for Name inputs
first_name = input('First Name? ')
last_name = input('Last Name? ')


#prompting user what is happening
print(f'Hello {first_name} {last_name} you will enter {NUM_SCORES} scores and I will calculate the average for you.')

#asking for Score Inputs
score1 = int(input('Enter score 1: '))
score2 = int(input('Enter score 2: '))
score3 = int(input('Enter score 3: '))

#completing average calculation
avg = (score1 + score2 + score3 )/NUM_SCORES

#printing result
print(f'{first_name} {last_name} Your average score is {avg}. Congrats or Condolences as appropriate.')



