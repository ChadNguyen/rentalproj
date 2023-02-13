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

def Income(self):
    self.rental_income = int(input('What is your rental income?: '))
    if self.rental_income >=0:
        print(f"Your monthly rental income is {self.rental_income}")
    elif self.rental_income == 0:
        print('There is no Income from rentals.')
    else:
        print("Invalid input, please try again.")
    self.laundry = int(input('What is your laundry income?: '))
    if self.laundry >=0:
        print(f"Your monthly laundry income is {self.laundry}")
    elif self.laundry == 0:
        print('There is no Income from laundry.')
    else:
        print("Invalid input, please try again.")
    self.storage = int(input('What is your storage income?: '))
    if self.storage >=0:
        print(f"Your monthly storage income is {self.storage}")
    elif self.storage == 0:
        print('There is no Income from rentals.')
    else:
        print("Invalid input, please try again.")
    self.misc = int(input('What is your misc income?: '))
    if self.misc >=0:
        print(f"Your monthly miscellaneous income is {self.misc}")
    elif self.misc == 0:
        print('There is no Income from miscellaneous.')
    else:
        print("Invalid input, please try again.")

def expenses(self):
    print("Let's take a look at the expenses.")
    self.taxes = int(input('How much is your taxes?: '))
    if self.taxes >= 0:
        print(f"Your monthly taxes is {self.taxes}")
    else:
        print("Invalid input, please try again.")
    self.insurance = int(input('How much is your insurance?: '))
    if self.insurance >= 0:
        print(f"Your monthly insurance is {self.insurance}")
    else:
        print("Invalid input, please try again.")
    self.hoa_fee = int(input('How much is your HOA fee?: '))
    if self.hoa_fees >= 0:
        print(f"Your monthly hoa fee expense is {self.hoa_fees}")
    elif self.hoa_fees == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    self.lawn_snow = int(input('How much is your lawn/snow fee?: '))
    if self.lawn_snow >= 0:
        print(f"Your monthly lawn/snow expense is {self.lawn}")
    elif self.lawn_snow == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    self.vacancy = int(input('How much is your vacancy?: '))
    if self.vacancy >= 0:
        print(f"Your investment property's unrealized income potential is {self.vacancy}")
    else:
        print("Invalid input, please try again.")
    self.repairs = int(input('How much are your repairs?: '))
    if self.repairs >= 0:
        print(f"Your monthly repair expense is {self.repairs}")
    elif self.repairs == 0:
        print('There were no expenses in this department.')
    else:
        print("Invalid input, please try again.")
    self.cap_ex = int(input('How much is your capital expenditure?: '))
    if self.cap_ex >= 0:
        print(f"Your monthly capital expenditure espense is {self.cap_ex}")
    elif self.cap_ex == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    self.property_management = int(input('How much is your property management?: '))
    if self.property_management >= 0:
        print(f"Your monthly property management fee is {self.property_management}")
    elif self.property_management == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    self.electric = int(input('How much is your electricity?: '))
    if self.electric >= 0:
        print(f"Your monthly electric expense is {self.electric}")
    else:
        print("Invalid input, please try again.")
    self.water = int(input('How much is your water expense?: '))
    if self.water >= 0:
        print(f"Your monthly water expense is {self.water}")
    else:
        print("Invalid input, please try again.")
    self.sewer = int(input('How much is the sewer expense?: '))
    if self.sewer >= 0:
        print(f"Your monthly sewer expense is {self.sewer}")
    else:
        print("Invalid input, please try again.")
    self.garbage = int(input('How much is your garbage?: '))
    if self.garbage >= 0:
        print(f"Your monthly garbage expense is {self.garbage}")
    else:
        print("Invalid input, please try again.")
    self.gas = int(input('How much is your gas?: '))
    if self.gas >= 0:
        print(f"Your monthly gas expense is {self.gas}")
    else:
        print("Invalid input, please try again.")
    if self.electric >= 0:
        print(f"Your monthly electric expense is {self.electric}")
    else:
        print("Invalid input, please try again.")
    if self.gas >= 0:
        print(f"Your monthly gas expense is {self.gas}")
    else:
        print("Invalid input, please try again.")
    if self.hoa_fees >= 0:
        print(f"Your monthly hoa fee expense is {self.hoa_fees}")
    elif self.hoa_fees == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    if self.lawn_snow >= 0:
        print(f"Your monthly lawn/snow expense is {self.lawn}")
    elif self.lawn_snow == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    if self.vacancy >= 0:
        print(f"Your investment property's unrealized income potential is {self.vacancy}")
    else:
        print("Invalid input, please try again.")
    if self.repairs >= 0:
        print(f"Your monthly repair expense is {self.repairs}")
    else:
        print("Invalid input, please try again.")
    if self.cap_ex >= 0:
        print(f"Your monthly capital expenditure espense is {self.cap_ex}")
    elif self.cap_ex == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    if self.property_management >= 0:
        print(f"Your monthly property management fee is {self.property_management}")
    elif self.property_management == 0:
        print('There were no expenses spent in this department.')
    else:
        print("Invalid input, please try again.")
    if self.mortgage_payment >= 0:
        print(f"Your monthly mortgage is {self.mortgage_payment}")
    else:
        print("Invalid input, please try again.")
    self.total_monthly_expenses = self.taxes + self.insurance + self.water + self.garbage + self.electric + self.gas + self.hoa_fees + self.lawn + self.vacancy + self.repairs + self.cap_ex + self.property_management + self.mortgage_payment
    print(f"The total monthly expense is {self.total_monthly_expenses}")


class roi():
    def __init__(self):
        self.total_investment = 0
        self.monthly_cashflow = 0

    def investmentcost(self):
        print('Please answer a few questions to get an accurate Cash on Cash return of investment.')
        down_payment = int(input('What was the down payment for the property?: '))
        self.down_payment = int(down_payment)
        closing_cost = int(input('What was the closing cost on the property?: '))
        self.closing_cost = (closing_cost)
        reno_cost = int(input('Was there any renovation costs?: '))
        self.reno_cost = int(reno_cost)
        print('Here are the final results.')
        self.Total_Investment = self.down_payment + self.closing_cost + self.reno_cost 
        print('Total Investment spent on this property: {}'.format(self.Total_Investment))

    def cashflow(self):
        self.total_monthly_income = int(input("Enter the total monthly income: "))
        self.total_monthly_expenses = int(input("Enter the total monthly expenses: "))
        self.total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f"The total monthly cash flow is {self.total_monthly_cash_flow}")
        self.annual_cashflow = self.total_monthly_cash_flow * 12 #12months
        print(f"The total annual cash flow is {self.annual_cashflow}")
        self.roipercentage = "{:.2f}".format(float(self.annual_cashflow / self.Total_Investment * 100))
        print(f'The return of investment is {self.roipercentage}%')
    
property_investment = roi()
property_investment.investmentcost()
property_investment.cashflow()