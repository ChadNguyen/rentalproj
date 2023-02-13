class Mortgage:
    def __init__(self, interestRate, months, amount):
        self.interestRate = float(interestRate)
        self.months = int(months)
        self.amount = float(amount)
        
    def mortgage_payment(self):
        mortgage_loan = int(input('How much is the loan you are taking out for the Property?: '))
        mortgage_months_input = input('Is it a 15 year term or 30 year term:  ')
        if mortgage_months_input == '15':
            mortgage_months = 15 * 12
        elif mortgage_months_input == '30':
            mortgage_months = 30 * 12
        else:
            print('You can also enter in a custom term.')
            mortgage_months = int(input('Enter amount of Months for term:  '))
        mortgage_interest_rate = float(input('What is the interest rate?: '))
        mortgage_interest_rate = mortgage_interest_rate / 100 / 12
        mortgage_payment = mortgage_loan * mortgage_interest_rate * ((1 + mortgage_interest_rate) ** mortgage_months) / (((1 + mortgage_interest_rate) ** mortgage_months) - 1)

        print('The Monthly Payment of a ${:.2f} loan at {:.2f}%, is ${:.2f} for a {} month term.'.format(mortgage_loan, mortgage_interest_rate * 100 * 12, mortgage_payment, mortgage_months))
        
mortgage = Mortgage(0, 0, 0)
mortgage.mortgage_payment()



        

