# pseudocode

# import files
from user_interface import UserInterface
from addition import Addition

# start loop
while True:

    # make objects
    inter = UserInterface()
    sum = Addition()

    # start

    # ask user input1
    num1 = inter.input_user()
    # ask user input2
    num2 = inter.input_user()

    # call methods
    sum = sum.add(num1, num2)

    # print methods
    inter.print_sum(sum)