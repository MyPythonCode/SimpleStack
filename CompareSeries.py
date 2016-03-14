"""
This Program Get From The User Two Series Of Numbers
if the every element in the second series is a square value of
the first series element then we print the sum of each pair
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# strings defenition

command_str = "\nEnter number :\n>> "

exit_str = 'exit the program'
no_match_str = '\n~~~~~~~~~~\nNo Match !\n~~~~~~~~~~\n'
first_open_str = """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Welcome To Compare Series Program ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

open_str = """
----------------------------
Enter New Series of numbers:
----------------------------

Usage: [number] (enter)
Enter (-1) to finish the Series of numbers

Enter number :
>>"""

# end of strings defenition
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

first_series = []
second_series = []

print(first_open_str)

# get from the user the first series
user_input = int(input(open_str))

while user_input != -1:
    first_series.append(user_input)
    user_input = int(input(command_str))

# get from the user the second series
user_input = int(input(open_str))

while user_input != -1:
    second_series.append(user_input)
    user_input = int(input(command_str))

sum_series = []

# using zip to iterate two lists
for a , b in zip(first_series, second_series):
    if a*a == b:
        sum_series.append(a+b)

# check if the new series has the same size as the first and the second series
# if it has the same size then every element in the second series in a power of the
# first series elements
if len(first_series) != 0:
    if len(sum_series) == len(first_series):
        print('\n~~~~~~~~~~')
        print(sum_series)
        print('~~~~~~~~~~\n')
    else:
        print(no_match_str)

print(exit_str)