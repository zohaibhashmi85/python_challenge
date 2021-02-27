import csv
import os

input_file = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("Analysis", "budget_analysis.txt")


month_count = 0
sum_of_pl= 0
month_count_change =0
month_change = 0
before_month = 0
greatest_increase = 0
greatest_decrease = 0



with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        month_count += 1
        sum_of_pl +=int(row[1])

        if month_count > 1:
            month_change = int(row[1]) - before_month
        month_count_change += month_change
        before_month = int(row[1])

        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]

        if month_change < greatest_decrease:

            greatest_decrease = month_change
            greatest_decrease_month = row[0]

average= round(month_count_change / (month_count-1),2)


output = (
    f"Financial Analysis\n"
    f"---------------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total : ${sum_of_pl}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase : {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease : {greatest_decrease_month} (${greatest_decrease})\n"
     )
print(output)
with open(output_file, "w") as txt_file:
    txt_file.write(output)


