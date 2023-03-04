import sys

argument = sys.argv
arg_amount = len(argument)

if arg_amount <= 1:
    print("Ther's no arguments, its just a normal script")
elif argument[1] == "list" and arg_amount > 2:
    for element in argument[2]:
        print(element)