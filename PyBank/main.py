import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    total_months = 0
    net_total = 0
    profit_losses = []
    months = []
    for row in csv_reader:
        total_months += 1
        net_total = net_total + int(row[1])
        profit_losses.append(int(row[1]))
        months.append(row[0])
    
    monthly_changes = []
    profit_losses_len = len(profit_losses)
    for i in range(len(profit_losses)):
        if i < (len(profit_losses) - 1):
            aux_change = profit_losses[i + 1] - profit_losses[i]
            monthly_changes.append(aux_change)
    
    average_change = round(sum(monthly_changes) / len(monthly_changes), 2)
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    greatest_increase_month_index = monthly_changes.index(greatest_increase) + 1
    greatest_decrease_month_index = monthly_changes.index(greatest_decrease) + 1

    greatest_increase_month = months[greatest_increase_month_index]
    greatest_decrease_month = months[greatest_decrease_month_index]

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total : ${net_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

file = open('Analysis/Analysis_Results.txt', 'w')
file.write('Financial Analysis\n')
file.write('----------------------------\n')
file.write('Total Months: ' + str(total_months) + '\n')
file.write('Total : $' + str(net_total) + '\n')
file.write('Average Change: $' + str(average_change) + '\n')
file.write('Greatest Increase in Profits: ' + greatest_increase_month + ' ($' + str(greatest_increase) + ')\n')
file.write('Greatest Decrease in Profits: ' + greatest_decrease_month + ' ($' + str(greatest_decrease) + ')\n')
file.close()