# Die with zero Calculator

import tkinter as tk
from tkinter import simpledialog, messagebox

import matplotlib.pyplot as plt

expected_years_till_death = 0
social_security = 0
rate_of_return = .07
rate_of_return_in_retirement = .04

# Get an integer input from the user (requires type conversion)
#cash_investment = int(input("What expected retirement total? "))
#monthly_spend = int(input("What is your monthly spend in retirement? "))
#expected_years_till_death = int(input("What is your expected years to live in retirement? "))

# Pop-up input dialogs
monthly_spend = simpledialog.askinteger("Input", "What is your monthly spend in retirement?")
expected_years_till_death = simpledialog.askinteger("Input", "What is your expected years to live in retirement?")


annual_spend = monthly_spend *12

# Simulate each year of retirement
'''for i in range(expected_years_till_death):
    yearly_return = cash_investment * rate_of_return_in_retirement
    cash_investment += yearly_return
    cash_investment -= monthly_spend'''


# Calculate the present value (PV) needed to fund withdrawals
r = rate_of_return_in_retirement
n = expected_years_till_death
present_value = (annual_spend / r) * (1 - (1 + r) ** -n)



# Output result
#print(f"You will have ${cash_investment:,.2f} remaining at the end of your retirement.")

# Output result
#print(f"\nYou need ${present_value:,.2f} invested at retirement to withdraw ${monthly_spend:,.2f} per month for {n} years.\nAssumes a {r*100:.1f}% annual return on investments.")


# Show result in a pop-up
messagebox.showinfo("Result", f"You need ${present_value:,.2f} invested at retirement to withdraw ${monthly_spend:,.2f} per month for {n} years.\nAssumes a {r*100:.1f}% annual return.")

# Generate data for chart
years = list(range(n + 1))
balances = [present_value]
balance = present_value

for year in range(1, n + 1):
    balance = balance * (1 + r) - annual_spend
    balances.append(balance)

# Plot chart
plt.figure(figsize=(10, 6))
plt.plot(years, balances, marker='o', linestyle ='--', color='r')
plt.title("Investment Balance Over Retirement")
plt.xlabel("Years Into Retirement")
plt.ylabel("Investment Balance ($)")
plt.grid(True)
plt.tight_layout()
plt.show()