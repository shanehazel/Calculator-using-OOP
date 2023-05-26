# pseudocode

# import files
from user_interface import UserInterface
from addition import Addition
from subtraction import Subtraction

# start loop
while True:

    # make objects
    inter = UserInterface()
    sum = Addition()
    diff = Subtraction()

    # start

    # ask user input1
    num1 = inter.input_user()
    # ask user input2
    num2 = inter.input_user()

    # ask user for operation
    opt = inter.input_operation()

    # call methods
    sum = sum.add(num1, num2)
    diff = diff.subtract(num1, num2)

    # print methods
    if opt.lower() == "addition":
        inter.print_sum(sum)
    elif opt.lower() == "subtraction": 
        inter.print_diff(diff)