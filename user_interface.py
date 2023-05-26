# pseudocode 

# class UserInterface
class UserInterface:

    # def input_operation
    def input_operation(self):
        operation = str(input("\033[0;35;40m Choose one operation (Addition, Subtraction, Multiplication, Division): "))
        return operation

    # def input_user
    def input_user(self):
        num1 = float(input("\033[3;34;40m Enter number: "))
        # return input
        return num1

    # def print_sum
    def print_sum(self, sum1):
        # print sum
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(sum1) + "!" + "\033[1;33;40m     ==========")

    # def print_diff
    def print_diff(self, diff1):
        # print diff
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(diff1) + "!" + "\033[1;33;40m     ==========")

    # def print_product
    def print_product(self, product1):
        # print product
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(product1) + "!" + "\033[1;33;40m     ==========")

    # def print_quotient
    def print_quotient(self, quotient1):
        # print quotient
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(quotient1) + "!" + "\033[1;33;40m     ==========")

    # def retry
    def retry(self):
        inp = input(str("\033[0;33;40m Do you want to try again? (Yes or No): "))

        # if "yes" return True
        if inp.lower() == "yes":
            return True
        
        # else return False
        else: 
            print("\033[1;36;40m Thank you!")
            return False