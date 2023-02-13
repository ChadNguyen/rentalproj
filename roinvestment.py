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