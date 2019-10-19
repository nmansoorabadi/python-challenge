import os
import csv


month_count = 0
total_revenue = 0
this_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

# Read and open CSV file
csv_path = os.path.join('PayBank', 'Resources', 'budget_data.csv')
with open(csv_path, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print (csvreader)

    # print the Header
    csv_header=next(csvreader)

    # gather monthly changes in revenue
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_revenue = int(row[1])
        total_revenue = total_revenue + this_month_revenue
        if month_count > 1:
            revenue_change = this_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = this_month_revenue

# analyze the month by month results
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

# print summary to user
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

# save summary to txt

output_path = os.path.join("PayBank", "output", "new_analysis_data.csv")
with open(output_path,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: ${total_revenue}" + "\n")
    text.write(f"Average Revenue Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Revenue: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})" + "\n")