class UserInterface:

    def input_operation(self):
        operation = str(input("\033[0;35;40m Choose one operation (Addition, Subtraction, Multiplication, Division): "))
        return operation

    def input_user(self):
        num1 = float(input("\033[3;34;40m Enter number: "))
        return num1

    def print_sum(self, sum1):
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(sum1) + "!" + "\033[1;33;40m     ==========")

    def print_diff(self, diff1):
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(diff1) + "!" + "\033[1;33;40m     ==========")

    def print_product(self, product1):
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(product1) + "!" + "\033[1;33;40m     ==========")

    def print_quotient(self, quotient1):
        print("\033[1;32;40m Your number is", "\033[1;33;40m ==========     " + str(quotient1) + "!" + "\033[1;33;40m     ==========")

    def retry(self):
        inp = input(str("\033[0;37;40m Do you want to try again? (Yes or No): "))
        if inp.lower() == "yes":
            return True
        else: 
            print("\033[1;36;40m Thank you!")
            return False