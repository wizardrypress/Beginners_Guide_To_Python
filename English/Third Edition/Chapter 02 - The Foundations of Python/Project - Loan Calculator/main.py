# Loan Payment Calculator

# Input: Get user input for loan details
purchase_amount = float(input("Enter purchase amount: "))
annual_interest_rate = float(input("Annual interest rate: ")) / 100
loan_duration_years = int(input("Loan duration (years): "))
include_down_payment = input("Include down payment? (y/n): ")

down_payment = 0
if include_down_payment == 'y' or include_down_payment == 'Y':
    down_payment = float(input("Down payment amount: "))

# Calculate the loan amount
loan_amount = purchase_amount - down_payment

# Monthly interest rate calculation
monthly_interest_rate = annual_interest_rate / 12

# Total number of payments
total_payments = loan_duration_years * 12

# Car loan monthly payment calculation
monthly_payment = ((loan_amount * monthly_interest_rate) /
                   (1 - (1 + monthly_interest_rate) ** -total_payments))

# Output: Loan Details
print("\nLoan Details:")
print("\tPurchase Amount: ${:.2f}".format(purchase_amount))
print("\tDown Payment: ${:.2f}".format(down_payment))
print("\tLoan Amount: ${:.2f}".format(loan_amount))
print(f"\tNumber of Payments: {total_payments} ({loan_duration_years} years)")
print("\tInterest Rate: {:.3f}".format(annual_interest_rate*100))
print("\tMonthly Payment: ${:.2f}".format(monthly_payment))
