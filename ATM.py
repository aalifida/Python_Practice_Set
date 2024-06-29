class Atm:
    def __init__(self):
        self.__balance = 0
        self.__pin = "1223"


    def get_pin(self):
        return self.__pin
    

    def set_pin(self,newPin):
        if(type(newPin)==str and len(newPin)== 4):
            self.__pin=newPin
            print("Pin Changed")
        else:
            print("Invalid Pin")
    

    def __menu(self):
            userInput = input("""
             How would you like to proceed??
             For Pin Setting Press 1
             For Deposit Press 2
             For Withdraw Press 3
             For Balance Enquiry Press 4
             To Cancel Press 5
             """)
            if userInput == "1":
                self.create_pin()
            elif userInput == "2":
                self.deposit_balance()
            elif userInput == "3":
                self.withdraw_balance()
            elif userInput == "4":
                self.view_balance()
            elif userInput == "5":
                print("Good Bye")
            else:
                print("Invalid Option, Please Try Again")

    def create_pin(self):
        self.__pin = input("Enter Your New Pin: ")
        print("Pin Created Successfully")

    def deposit_balance(self):
        user_enteredpin = input("Please Enter Your 4 digit pin: ")
        if user_enteredpin == self.__pin:
            amount = int(input("Enter amount of money you want to deposit: "))
            self.__balance += amount
            print("Deposit Successful")
        else:
            print("Incorrect Pin")

    def withdraw_balance(self):
        user_enteredpin = input("Please Enter Your 4 digit pin: ")
        if user_enteredpin == self.__pin:
            amount = int(input("Enter amount of money you want to Withdraw: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdraw Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect Pin")

    def view_balance(self):
        user_enteredpin = input("Please Enter Your 4 digit pin: ")
        if user_enteredpin == self.__pin:
            print(f"Your balance is: {self.__balance}")
        else:
            print("Invalid Pin")

# Create an instance of the ATM class
aali = Atm()
aali.set_pin("2093")
print(aali.get_pin())
