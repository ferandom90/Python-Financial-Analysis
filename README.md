# python-challenge

This Python script reads a CSV file containing financial data, processes it, and prints out some financial analysis results. The code imports the built-in csv module to read the CSV file and then opens the file using the open() function. The CSV file path is specified in the code, PayBank = "/Users/fernandoescamilla/python-challenge/PyBank/Resources/budget_data.csv". and PyPoll = "/Users/fernandoescamilla/python-challenge/PayPoll/Resources/budget_data.csv"

The script reads the file using csv.reader(), obtains the header of the document and stores it in a list called header. It then creates these lists: periods, dates, and amounts. These lists are used to obtain the year (in periods), the full date (in dates), and the financial amount (in amounts) of each row in the CSV file.

After that, the code loops through all rows in the CSV file using a for loop, and obtains the total number of months by incrementing row_counter for each row. It also obtains the total amount of financial profit or loss by adding each row's profit/loss value to the total_amount variable.

In the loop, the code obtains the year value from the Date column and appends it to the periods list if it is not already present. It then appends the full date to the dates list and the financial amount to the amounts list.

The script then calculates the average change by dividing the total_amount variable by the row_counter variable.

Next, the code finds the greatest increase in profits and the greatest decrease in losses by looping through the amounts list and checking if the current amount is greater than or less than the current highestAmount and lowestAmount, respectively.

Finally, the script prints out the financial analysis results, including the total number of months, the total amount of financial profit or loss, the average change, the greatest increase in profits, and the greatest decrease in losses. It also creates a text file named py_bank_file.txt in the specified directory, prints the financial analysis results to it. 