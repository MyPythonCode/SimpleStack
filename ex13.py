"""this program print only the positive numbers from the user input - series of values"""

def is_int(a):
    """this function checks if the argument is number"""
    if a.isdigit():
        only_int.append(a)

only_int = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# strings defenition

command_str = "\nEnter number :\n>> "

exit_str = 'exit the program'

no_num_str = "No Integers"

first_open_str = """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Welcome To Print Only Positive Numbers Program ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

open_str = """
Usage: [value] (enter)
Enter (-1) to finish the Series of numbers

Enter value :
>>"""

# end of strings defenition
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

user_values = []

print(first_open_str)

user_input = input(open_str)

while 1==1:
    """this loop breaks when the user series end with (-1)"""
    if user_input == '-1':
        break

    user_values.append(user_input)
    user_input = input(command_str)

for x in user_values:
    is_int(x) # function that check if the value is int

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
if len(only_int) == 0:
    print(no_num_str)
else:
    print(only_int)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print(exit_str)

