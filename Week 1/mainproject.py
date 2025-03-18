
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Interest Rate (in %): "))
T = float(input("Enter Time Period (in years): "))
n = int(input("Enter number of times interest is compounded per year: "))
PMT = float(input("Enter periodic payment amount for annuity: "))

def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P, R, n, t):
    A = P * (1 + R / n) ** (n * t)
    return A

def annuity_plan(PMT, R, n, t):
    A = PMT * (((1 + R / n) ** (n * t) - 1) / (R / n))
    return A

simple_A = simple_interest(P, R, T)
compound_A = compound_interest(P, R / 100, n, T)
annuity_A = annuity_plan(PMT, R / 100, n, T)

print(f"Simple Interest Amount: {simple_A}")
print(f"Compound Interest Amount: {compound_A}")
print(f"Annuity Plan Amount: {annuity_A}")
