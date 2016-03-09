open_str = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Welcome To My Python Stack ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage: [i] or [e] or [p] :

[i] - Insert value to stack
[e] - Remove value from stack
[p] - Print the stack
\n>>"""

stack = []

while 1 == 1:

    user_input = str(input(open_str))

    if user_input == 'i':

        user_input = str(input("\nEnter value :\n\n>> "))
        stack.append(user_input[1:])

    elif user_input == 'e':

        if len(stack) == 0:
            break;

        stack.pop()

    elif user_input == 'p':

        print('\n\n*********************\nThe Stack values are:\n')

        if len(stack) == 0:
            print('***    Empty !    ***')

        for i , a in enumerate(stack):
            print(i, a)

        print('*********************\n')

    else:

        print('\n\n~~~~~~~~~~~~~~~~~~~\n~ WRONG INPUT !!! ~\n~~~~~~~~~~~~~~~~~~~\n')

