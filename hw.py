class rent:
    def __init__(self, income, expense):
        self.income = income
        self.expense = expense
        self.cashflow = 0



        self.total_expense = [0]
        self.total_income = [0]

    def add_income(self):
        
        incomename = input("What is the income name?: ")
        incomeamount= int(input("What is the income amount?: "))
        self.income = incomeamount
        self.total_income.append(self.income)
        incomecontd = input("Do you want to enter another income?(type: y or n): ")
        if incomecontd == "y":
            self.add_income()

        else:
            print(self.income)
            print(' Total income is:', sum(self.total_income))
        
    

    def add_expense(self):
        expensename = input("What is the expense name?: ")
        expenseamount= int(input("What is the expense amount?: "))
        self.expense = expenseamount
        self.total_expense.append(self.expense)
        expensecontd = input("Do you want to enter another expense?(type: y or n): ")
        if expensecontd == "y":
            self.add_expense()

        else:
            print(self.expense)
            print('Total expense is:', sum(self.total_expense))



    def totalcashflow(self):
        
        print('Total cashflow is:'+( sum(self.total_income) - sum(self.total_expense)))

    
    
    def show_expense(self):
        print(self.expense)
    
    def show_income(self):
        print(self.income)




rentG = rent(0,0)

rentG.add_income()
rentG.add_expense()
rentG.totalcashflow