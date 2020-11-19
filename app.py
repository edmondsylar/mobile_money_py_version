from time import sleep
from os import system as sys
# Mobile money illustrated
# I have eariler mentioned using functins (OOP) {classes and Functions} so
# am going to demonstrate that down here as well.


# we have created a class called mobile money to house all our operations


class Mobile_Money:
    def __init__(self):
        self.bal = 0
        self.transactions = []
    # function for creating making a deposit
    def deposit(self, amount):
        # make sure a person can't deposit 0 shs
        if(amount <= 0):
            return ('error, cannot deposit 0 shs')

        # now here lets increment the balance.
        self.bal += amount
        return "Deposit of {} made \nNew account balance is {}".format(amount, self.bal)

    # function to check the balance.
    def check_balance(self):
        return "Your account balance is {} \n".format(self.bal)


    # you can use this functinn to log the transactions.
    def transaction_log(self, trans):
        return False


    # function to make a withdraw
    def withdraw(self, amount):
        # we gonna need a function that handles the withdraw charges.
        # in this case since the funciton will only be called by this function,
        # we are going to embed the function within this function.
        #  function name { charges }.
        def charges(amount):
            # this function will be returning the actual withdraw and the charge
            if(amount <= 10000):
                charge = 800
                return [amount + 800, 800]
            # for the value of time we are only going to validate 10,000 and default the rest to have a charge of
            # 1,200
            else:
                return [amount + 1200, 1200]


        # we post to make a number of validation here ie
        # 1.withdraw not greater than bal
        # 2.withdraw not equal to balance and more

        # this calls the charges function and passes the amount we need to withdraw and returns
        # the amount plus the withdraw and also the actual charge
        withd = charges(amount)

        # now we validate the amount+withdraw charges are not greater than the balance
        if(withd[0] == self.bal):
            return 'you have Insurficient balance on your account'
        elif(withd[0] > self.bal):
            return 'you have Insurficient balance on your account'

        self.bal -= withd[0]
        return '\nWithdraw of {} made \nat a charge of {} \nNew balance is {}\n'.format(amount, withd[1], self.bal)


user = Mobile_Money()

# lets create our menu donw here.
while True:
    print('1. Deposit Amount \n2. Make a withdraw \n3. Check balance \n4. Clear Screen')
    option = int(input("Select Option: "))
    if(option == 1):
        amount = int(input("Enter amount: "))
        print(user.deposit(amount))
        sleep(2)
    elif(option == 2):
        amount = int(input("Enter Deposit amount: "))
        print(user.withdraw(amount))
        sleep(2)

    elif(option == 3):
        print(user.check_balance())
        sleep(2)

    elif(option == 4):
        try:
            sys('clear')
        except expression as identifier:
            sys('cls')
        sleep(1)
