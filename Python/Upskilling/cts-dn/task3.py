salary = 75000.5
tax_rate = 0.18

def calculate_tax(salary, tax_rate):
    tax_amount = salary * tax_rate
    return tax_amount
tax = calculate_tax(salary, tax_rate)
print(f"The tax amount on a salary of {salary:.2f} at a tax rate of {tax:.2f}")