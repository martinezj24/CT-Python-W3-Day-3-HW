class BudgetCategory:

    def __init__(self, budget, category):
        self.__budget = budget
        self.__category = category
        self.__expenses = 0

    # Task 2: Implement Getters and Setters
    
    def get_budget(self):
        return self.__budget
    
    def set_budget(self, budget): #Not sure how to have my else statement trigger for negative ints, please advise, thank you!
        if budget >= 0:
            self.__budget = budget
        else:
            print('Invalid Input. Try again')
    
    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        self.__category = category

    # Task 3: Add Budget Functionality

    def add_expense(self, amount):
        if amount >= 0:
            self.__expenses += amount
            print(f"\nYou've spent ${amount} on {self.__category}")
        else:
            print('Invalid input. Try again')

    # Task 4: Display Budget Details

    def display_category_summary(self):
        budget_remaining = self.__budget - self.__expenses
        print(f"Current Category: {self.__category}")
        print(f"Current Budget: ${self.__budget}")
        print(f"Current Expenses: {self.__expenses}")
        print(f"Budget Remaining: ${budget_remaining}")


utilities = BudgetCategory(-10, 'Utilities')
utilities.add_expense(100)
utilities.display_category_summary()