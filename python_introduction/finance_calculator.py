monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your total monthly expenses: "))
monthlySavings = monthlyIncome - monthlyExpenses
annualSavings = monthlySavings * 12 + int((monthlySavings * 12 * 0.05))
print(f"Your monthly savings are ${monthlySavings}.")
print(f"Projected savings after one year, with interest, is: ${annualSavings}.")
