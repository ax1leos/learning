import csv

totals = {}
with open("expenses.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["category"] not in totals:
           totals[row["category"]] = float(row["amount"])
        else:
            totals[row["category"]] += float(row["amount"])
 
total_sum = 0        
for category, total_amount in totals.items():
    total_sum += total_amount
    print(f"{category}: {total_amount}")
print(f"Total: {total_sum}")