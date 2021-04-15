import csv

def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data
def run():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    highest_sale = max(sales)
    lowest_sale = min(sales)
    month = []
    for row in data:
        months = str(row['month'])
        month.append(months)
    expenditure = []
    for row in data:
        expense = int(row['expenditure'])
        expenditure.append(expense)
    
    #For loop prints the total sales across each month
    print('Months Sales')
    for months, sale in zip(month, sales): 
        print(months,sale)
    
    print('Total sales: €{}'.format(total))
    print('Average sales: €{}'.format((round(total/12, 2))))
    
    #For loops to find the highest and lowest sale months
    for months, sale in zip(month, sales):
        if sale == max(sales):
            print('Highest sale month: {}'.format(months))
            print('Highest sale: €{}'.format(highest_sale))
    for months, sale in zip(month, sales):    
        if sale == min(sales):
            print('Lowest sale month: {}'.format(months))
            print('Lowest sale: €{}'.format(lowest_sale))
     
    # Monthly Profit
    yearly_profit = 0
    print('Monthly Profit in €')
    for sale, expense in zip(sales, expenditure):
        monthly_profit = sale - expense
        print(monthly_profit)
        yearly_profit = yearly_profit + monthly_profit
    print('Yearly profit: €{}'.format(yearly_profit))
    
    #Monthly Sale Changes as percentages
    print('Monthly Sale Changes as Percentages (%)')
    i = 0
    for sale in sales:
        percentage_diff=((sales[i+1] - sales[i])/sales[i]) * 100
        print(round(percentage_diff, 2))
        i = i + 1
run()


