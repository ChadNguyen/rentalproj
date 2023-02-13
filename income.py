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