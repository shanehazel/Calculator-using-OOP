from user_interface import UserInterface

class Tagalog(UserInterface):
    def input_operation(self):
        operation = str(input("\033[0;35;40m Pumili ng gagamiting operasyon (Addition, Subtraction, Multiplication, Division): "))
        return operation

    def input_user(self):
        num1 = float(input("\033[3;34;40m Ibigay ang iyong numero: "))
        return num1

    def print_sum(self, sum1):
        print("\033[1;32;40m Ang iyong panibagong numero ay", "\033[1;33;40m ==========     " + str(sum1) + "!" + "\033[1;33;40m     ==========")

    def print_diff(self, diff1):
        print("\033[1;32;40m Ang iyong panibagong numero ay", "\033[1;33;40m ==========     " + str(diff1) + "!" + "\033[1;33;40m     ==========")

    def print_product(self, product1):
        print("\033[1;32;40m Ang iyong panibagong numero ay", "\033[1;33;40m ==========     " + str(product1) + "!" + "\033[1;33;40m     ==========")

    def print_quotient(self, quotient1):
        print("\033[1;32;40m Ang iyong panibagong numero ay", "\033[1;33;40m ==========     " + str(quotient1) + "!" + "\033[1;33;40m     ==========")

    def retry(self):
        inp = input(str("\033[0;37;40m Nais mo pa bang umulit? (Oo o Hindi): "))
        if inp.lower() == "oo":
            return True
        else: 
            print("\033[1;36;40m Maraming Salamat!")
            return False