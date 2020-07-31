#BANK ACCOUNT CLASS
#a script to simulate a typical bank account

class BankAccount:
    #__init__ initializes the method. It accepts an input as account's current balance
    #and assigns it to the attribute __currentbalance
    def __init__(self, balance):
        self.__currentbalance = balance
    
    #deposit method accepts input and adds it to the __currentbalance attribute
    def deposit(self, amount_deposited):
        self.__currentbalance += amount_deposited
    
    #withdraw method regulates all withdrawals made from the account
    def withdraw(self, amount_to_withdraw):
        if self.__currentbalance >= amount_to_withdraw:
            self.__currentbalance -= amount_to_withdraw
        else:
            print('Insufficient Funds!')
    
    #account_balance method stands to display the account balance of the account after 
    #every transaction
    def account_balance(self):
        return self.__currentbalance
    
    #indicating the final answer as a string
    def __str__ (self):
        return 'Your account balance is ' + format(self.__currentbalance, '.2f')

def main():
    my_account = eval(input('type your current balance: '))

    save_funds = BankAccount(my_account)

    deposit_funds = eval(input('how much do you want to deposit?: '))
    save_funds.deposit(deposit_funds)
    print('your current balance is: N', format(save_funds.account_balance(), ',.2f'))

    user_choice = input('Do you want to withdraw? \n YES or NO: ' )
    user_choice = user_choice.upper()

    if user_choice == 'YES':
        withdrawal = eval(input('How much do you want to withdraw? '))
        save_funds.withdraw(withdrawal)
        print('your current balance is: N', format(save_funds.account_balance(), ',.2f'))

    else:
        pass
    print(save_funds)
    print('Have a nice day!')
    

main()
