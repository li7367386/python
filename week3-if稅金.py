# 所得低於10000繳2%，大於的部分繳8%稅金

print("Please enter your income:")
income = float(input())

if income <= 10000:
    tax = income * 0.02
if income > 10000:  # else better
    tax = (income - 10000) * 0.08 + 200
print("Tax amount:$" + str(tax))
