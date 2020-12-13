# export PYTHONPATH = '/home/bogdan/Desktop/Python/secure-erp-practice/'
# import sys
# sys.path.append('/home/bogdan/Desktop/Python/')

from model.crm import crm
from view import terminal as view
from model import data_manager
from model import util

def list_customers():
    print(crm.HEADERS)
    element_list = data_manager.read_table_from_file(crm.DATAFILE)
    for row in element_list:
        print(row, end='\n')
    # view.print_error_message("Not implemented yet.")
    # print('x')


def add_customer():
    tabular = []
    name_list = []
    email_list = []
    subscribed_list = []
    id_list = []
    name = input('Please provide a name: ')
    name_list.append(name)
    email = input('Please provide an email: ')
    email_list.append(email)
    subscribed_status = input('Please provide a subscribed status (1: yes, 0: no): ')
    subscribed_list.append(subscribed_status)
    customer_id = util.generate_id()
    id_list.append(customer_id)
    tabular.append(id_list)
    tabular.append(name_list)
    tabular.append(email_list)
    tabular.append(subscribed_list)
    data_manager.write_table_to_file(crm.DATAFILE, tabular)
    
    view.print_error_message("Not implemented yet.")


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
