from model.sales import sales
from view import terminal as view
from model import data_manager
from model import util


def list_transactions():
    view.print_error_message("Not implemented yet.")


def add_transaction():
    view.print_error_message("Not implemented yet.")


def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    revenue = []
    element_list = data_manager.read_table_from_file(sales.DATAFILE)
    for row in element_list:
        revenue.append(row[3])
    index_of_biggest_revenue = revenue.index(max(revenue))
    transaction = element_list[index_of_biggest_revenue + 1]
    return transaction
    print(' '.join(transaction))



def get_biggest_revenue_product():
    biggest_transaction = get_biggest_revenue_transaction()
    product = biggest_transaction[2]
    print(product)


def count_transactions_between():
    dates = []
    first_date = view.get_input('Enter the first date (e.g. 2014-8-1): ')
    second_date = view.get_input('Enter the second date: ')
    element_list = data_manager.read_table_from_file(sales.DATAFILE)
    for row in element_list:
        dates.append(row[-1])
    count = 0
    for date in dates:
        if date > first_date and date < second_date:
            count +=1
    print(f'The number of transactions between {first_date} and {second_date} is: {count}!')

def sum_transactions_between():
    dates = []
    transactions_price = []
    indexes = []
    transactions_sum = []
    element_list = data_manager.read_table_from_file(sales.DATAFILE)
    first_date = view.get_input('Enter the first date (e.g. 2014-8-1): ')
    second_date = view.get_input('Enter the second date: ')
    for row in element_list:
        dates.append(row[-1])
        transactions_price.append(row[-2])
    for date in dates:
        if date > first_date and date < second_date:
            indexes.append(dates.index(date))
    for index in indexes:
        transactions_sum.append(transactions_price[index])
    transactions_sum = [float(i) for i in transactions_sum]
    result = sum(transactions_sum)
    print(f'The sum of transactions between {first_date} and {second_date} is: {result}')


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
