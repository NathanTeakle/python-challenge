import csv
import os

# Provide the source CSV file and read the data.
# Updated, I got the os path method to finally work!!!!
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Calculate the total number of months in the source CSV file.
total_months = len(data)

# Calculate the net total amount of "Profit/Losses" over the entire period.
net_total_PL = sum(int(row['Profit/Losses']) for row in data)

# Calculate the changes in "Profit/Losses" over the entire period.
changes = [int(data[i + 1]['Profit/Losses']) - int(data[i]['Profit/Losses']) for i in range(total_months - 1)]

# Calculate the average of those changes.
average_change_PL = sum(changes) / len(changes)

# Find the greatest increase in profits (date and amount) over the entire period.
greatest_increase = max(changes)
greatest_increase_date = data[changes.index(greatest_increase) + 1]['Date']

# Find the greatest decrease in profits (date and amount) over the entire period.
greatest_decrease = min(changes)
greatest_decrease_date = data[changes.index(greatest_decrease) + 1]['Date']

# Print the output to the terminal.
print(f'Total Months: {total_months}')
print(f'Total: ${net_total_PL}')
print(f'Average Change: ${average_change_PL:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

# Export the output of the terminal to a txt file in the 'Analysis' folder.
# The \n dictates where a new line should begin in the output.
outpath =  os.path.join("Analysis", "budget_analysis.txt")
with open(outpath, 'w') as file:
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${net_total_PL}\n')
    file.write(f'Average Change: ${average_change_PL:.2f}\n')
    file.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')
