def main():
    print(" This is a mothly payment loan calculator")
    print("")

    principal = float("input the loan amount: ")
    apr = input("Input the  annual interest rate:")
    years = int(input("Input the amount of years: "))


    monthly_interest_rate = apr/1200
    amount_of_months = years * 12
    monthly_payment = principal * (monthly_interest_rate/(1-(1 + monthly_interest_rate) ** (-amount_of_months)))

    print("The monthly payment for this loan is : %2f" %monthly_payment)