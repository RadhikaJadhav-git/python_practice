# Program to calculate Simple Interest and Compound Interest

def simple_interest(principal, rate, time):   #simple interest
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    """Calculate Compound Interest"""
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

def main():
    print("Simple and Compound Interest Calculator")

    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time (in years): "))


    si = simple_interest(principal, rate, time)
    ci = compound_interest(principal, rate, time)

    print(f"\nSimple Interest = {si:.2f}")
    print(f"Compound Interest = {ci:.2f}")

if __name__ == "__main__":
    main()
