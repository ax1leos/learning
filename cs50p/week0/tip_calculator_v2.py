total = input("How much was the meal?: ")
tip = input("What percentage would you like to tip?: ")

total = float(total.replace("$", ""))
tip = float(tip.replace("%", ""))
answer = total*tip/100

print(f"Leave: ${answer:.2f}" )
