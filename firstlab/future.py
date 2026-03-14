p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest (in decimal, ex: 0.05): "))
n = int(input("Enter number of years: "))

fv = p * (1 + r) ** n
print("Future value:",fv)