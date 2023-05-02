
import csv
from pathlib import Path

# Files to Input/Output
input_file = Path("resources/budget_data.csv")
output_file = Path("analysis/result_PyBank.txt")

# Reading the file
with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Initializing the variables
    count_row = 0
    total_revenue = 0
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}
    prev_revenue = None
    budget_chart = []

    # Iterating through CSV file
    for row in csvreader:
        date = row[0]
        revenue = int(row[1])
        count_row += 1
        total_revenue += revenue

        if prev_revenue is not None:
            change = revenue - prev_revenue
            budget_chart.append(change)

            # Finding the greatest increase in revenue
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # Finding the lowest increase in revenue
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        prev_revenue = revenue



    # Average Revenue Change
    avg_revenue = sum(budget_chart) / len(budget_chart)

    # Print the output
    print("\nFinancial Analysis")
    print("----------------------------")
    print(f"Total Months: {count_row}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${avg_revenue:.2f}")
    print(f"Greatest Increase in Revenue: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Revenue: {greatest_decrease['date']} (${greatest_decrease['amount']})")

    # Create Report Summary
    report = f"""Financial Analysis
----------------------------
Total Months: {count_row}
Total: ${total_revenue}
Average Change: ${avg_revenue:.2f}
Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})
Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})
"""

# Spit Out to Text File
with open(output_file, "w") as txtfile:
    txtfile.write(report)
