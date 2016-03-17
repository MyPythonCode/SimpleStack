"""
This Program makes A Simple Stack Using Lists
the program will exit when the stack is empty and the user insert 'e'
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# strings defenition

command_str = "\nEnter value :\n>> "

stack_str = '\n\n*********************\nThe Stack values are:\n'
empty_stack_str = '***    Empty !    ***\n*********************\n'
finish_stack_str = '*********************\n'
wrong_input_str = '\n\n~~~~~~~~~~~~~~~~~~~\n~ WRONG INPUT !!! ~\n~~~~~~~~~~~~~~~~~~~\n'

open_str = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Welcome To My Python Stack ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage: [i] or [e] or [p] :

[i] - Insert value to stack
[e] - Remove value from stack
[p] - Print the stack
\n>>"""

# end of strings defenition
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

stack = []

while 1 == 1:
    """this loop runs until the user try to remove value from the stack but the stack is empty"""

    user_input = str(input(open_str))

    if user_input == 'i':

        user_input = str(input(command_str))
        stack.append(user_input[1:])

    elif user_input == 'e':

        if len(stack) == 0:
            break;

        stack.pop()

    elif user_input == 'p':

        print(stack_str)

        if len(stack) == 0:
            print(empty_stack_str)
            continue

        for i , a in enumerate(stack):
            print(i, a)

        print(finish_stack_str)

    else:

        print(wrong_input_str)

