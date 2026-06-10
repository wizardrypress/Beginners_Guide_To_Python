# Project: Loan payment calculator
#
# Yeh project car loan ki monthly payment calculate karta hai.
# Isme optional down payment aur 0% interest rate dono handle kiye gaye hain.

purchase_amount = float(input("Purchase amount enter karein: "))
annual_interest_rate = float(input("Annual interest rate percentage mein enter karein: "))
loan_term_years = int(input("Loan ki duration years mein enter karein: "))

include_down_payment = input("Down payment include karni hai? (y/n): ").lower()

down_payment = 0.0

if include_down_payment == "y":
    down_payment = float(input("Down payment amount enter karein: "))

loan_amount = purchase_amount - down_payment
total_payments = loan_term_years * 12

if total_payments <= 0:
    print("Loan duration zero se zyada honi chahiye.")
elif loan_amount <= 0:
    print("Loan amount zero se zyada honi chahiye.")
else:
    if annual_interest_rate == 0:
        monthly_payment = loan_amount / total_payments
    else:
        monthly_interest_rate = (annual_interest_rate / 100) / 12

        numerator = loan_amount * monthly_interest_rate
        denominator = 1 - (1 + monthly_interest_rate) ** -total_payments
        monthly_payment = numerator / denominator

    print()
    print("Loan details:")
    print(f"    Purchase amount: Rs {purchase_amount:.2f}")
    print(f"    Down payment: Rs {down_payment:.2f}")
    print(f"    Loan amount: Rs {loan_amount:.2f}")
    print()
    print(f"    Number of payments: {total_payments} ({loan_term_years} years)")
    print(f"    Interest rate: {annual_interest_rate:.3f}%")
    print(f"    Monthly payment: Rs {monthly_payment:.2f}")
