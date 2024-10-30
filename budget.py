
# Online Python - IDE, Editor, Compiler, Interpreter

class Budget():
    def __init__(self, income = 0, savings = 0):
        self.income = income
        self.expenses = {}
        self.saving = savings
        self.budget = {}
    
    def update_budget(self):
        while True:
            expense_type = input("What kind of expenses is it?: ")
            if expense_type == "exit":
                break
            amount = float(input("What is the expense amount? "))
            if expense_type in self.budget:
                self.budget[expense_type] += amount
            else:
                self.budget[expense_type] = amount
        
    def update_expenses(self):
        while True:
            expense_type = input("What kind of expenses is it?: ")
            if expense_type == "exit":
                break
            amount = float(input("What is the expense amount? "))
            if expense_type in self.expenses:
                self.expenses[expense_type] += amount
            else:
                self.expenses[expense_type] = amount
    
    def total(self):
        print("You are total expenses are:")
        for key, values in self.expenses.items():
            print(f"{key}: {values}")
        print("------------------------")
        print(f"Total: {sum(self.expenses.values())}")
    
    def compare(self):
        print("Here is a comparison of your current expenses to your budgeted options")
        for (key, value), (expense, amount) in zip(self.budget.items(), self.expenses.items()):
            print(f"Budget: {key}: {value}  Actual expense: {expense}: {amount} Difference: {amount-value}")
            
    def savings_goals(self):
        print("Let's see how far you are on with your savings goals")
        print(f"Saving goals: {self.saving}")
        print(f"Current savings: {self.income-(sum(self.expenses.values()))}")
        

        

        
        