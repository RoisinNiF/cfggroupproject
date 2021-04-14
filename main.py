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
    print('Total sales: {}'.format(total))
    print('Average sales: {}'.format((round(total/12, 2))))
    month = []
    for row in data:
        months = str(row['month'])
        month.append(months)
    print('MONTHS')
    for months in month:
        print(months)
    print('SALES')
    for sale in sales: 
        print(sale)
     
    #Monthly Sale Changes as parcentage
    i = 0
    for sale in sales:
        percentage_diff=((sales[i+1] - sales[i])/sales[i]) * 100
        print(round(percentage_diff, 2))
        i = i + 1
run()


