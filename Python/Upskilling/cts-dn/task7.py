def floorDiv(total_bill, people):
    return total_bill // people
tot_bill = 1250
peop = 4
fd = floorDiv(tot_bill, peop)
print(f"Each person should pay: {fd}")