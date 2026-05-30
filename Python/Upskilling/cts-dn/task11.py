kg = float(input("Enter weight in kg: "))
def kg_to_lbs(kg):
    lbs = kg * 2.20462
    return lbs
kg_to_lbs(kg)
print(f"{kg} kg is equal to {kg_to_lbs(kg):.2f} lbs")