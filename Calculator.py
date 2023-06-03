from user_interface import UserInterface
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division
from user_interface_tagalog import Tagalog

while True:

        inter = UserInterface()
        sum = Addition()
        diff = Subtraction()
        product = Multiplication()
        quotient = Division()
        tag = Tagalog()

        # start
        ask = str(input("Choose language: Tagalog or English: "))

        if ask.lower() == "english":
            num1 = inter.input_user()
            num2 = inter.input_user()

            opt = inter.input_operation()

            sum = sum.add(num1, num2)
            diff = diff.subtract(num1, num2)
            product = product.multiply(num1, num2)
            quotient = quotient.divide(num1, num2)

            if opt.lower() == "addition":
                inter.print_sum(sum)
            elif opt.lower() == "subtraction": 
                inter.print_diff(diff)
            elif opt.lower() == "multiplication":
                inter.print_product(product)
            elif opt.lower() == "division":
                inter.print_quotient(quotient)

            if not inter.retry():
                break
        
        elif ask.lower() == "tagalog":
            num1 = tag.input_user()
            num2 = tag.input_user()

            opt = tag.input_operation()

            sum = sum.add(num1, num2)
            diff = diff.subtract(num1, num2)
            product = product.multiply(num1, num2)
            quotient = quotient.divide(num1, num2)

            if opt.lower() == "addition":
                tag.print_sum(sum)
            elif opt.lower() == "subtraction": 
                tag.print_diff(diff)
            elif opt.lower() == "multiplication":
                tag.print_product(product)
            elif opt.lower() == "division":
                tag.print_quotient(quotient)       

            if not tag.retry():
                break
    