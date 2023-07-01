import csv

# Open the CSV file
with open("..","Resources","budget_data.csv","r") as file:
    
    # Read the CSV file
    csv_reader = csv.reader(file)
    
    # Skip the header row
    header = next(csv_reader)
    
    # Initialize variables
    total_months = 0
    net_profit_loss = 0
    previous_profit_loss = 0
    changes = []
    max_increase = ['', 0]
    max_decrease = ['', 0]
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Increment the total number of months
        total_months += 1
        
        # Get the profit/loss value from the current row
        profit_loss = int(row[1])
        
        # Add the profit/loss to the net total
        net_profit_loss += profit_loss
        
        # Calculate the change in profit/loss from the previous month
        change = profit_loss - previous_profit_loss
        
        # Add the change to the list of changes
        changes.append(change)
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss
        
        # Check if the current change is the greatest increase
        if change > max_increase[1]:
            max_increase = [row[0], change]
        
        # Check if the current change is the greatest decrease
        if change < max_decrease[1]:
            max_decrease = [row[0], change]
    
    # Calculate the average change
    average_change = sum(changes) / len(changes)
    
    # Print the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total Amount: ${net_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})")
    print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")
