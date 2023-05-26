# pseudocode

# import files
from user_interface import UserInterface
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division

# start loop
while True:

    # make objects
    inter = UserInterface()
    sum = Addition()
    diff = Subtraction()
    product = Multiplication()
    quotient = Division()

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
    product = product.multiply(num1, num2)
    quotient = quotient.divide(num1, num2)

    # print methods
    if opt.lower() == "addition":
        inter.print_sum(sum)
    elif opt.lower() == "subtraction": 
        inter.print_diff(diff)
    elif opt.lower() == "multiplication":
        inter.print_product(product)
    elif opt.lower() == "division":
        inter.print_quotient(quotient)