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
# from constants import NUM_SCORES

#asking for Name inputs
first_name = input('First Name? ')
last_name = input('Last Name? ')

NUM_SCORES = int(input('How many things did you fail?? '))

#prompting user what is happening
print(f'Hello {first_name} {last_name} you will enter {NUM_SCORES} scores and I will calculate the average for you.')

#asking for Score Inputs
score = 0
for x in range(1, NUM_SCORES+1):
  score += int(input(f'Enter score {x}: '))


#completing average calculation
avg = (score )/NUM_SCORES

#printing result
print(f'{first_name} {last_name} Your average score is {avg}. Congrats or Condolences as appropriate.')

#tested with 100, 50, and 0 got 50.0 as a result
#tested with 20, 10, and 5 got 11.6666666667 as a result
#tested with -500, 9000000000, and 0 got 2999999833.3333335 as a result
#tested by entering letters in the scores section - got error due to not being able to conver to an int.
