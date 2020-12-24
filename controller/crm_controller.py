import csv #parca nu l-am folosit
from model.crm import crm
from view import terminal as view
from model import data_manager
from model import util

ID_COLUMN = 0
NAME_COLUMN = 1
EMAIL_COLUMN = 2
SUBSCRIBED_COLUMN = 3

def list_customers():
    element_list = data_manager.read_table_from_file(crm.DATAFILE)
    view.print_table(element_list, crm.HEADERS)



def add_customer():
    tabular = []
    name = input('Please provide a name: ')
    email = input('Please provide an email: ')
    subscribed_status = input('Please provide a subscribed status (1: yes, 0: no): ')
    customer_id = util.generate_id()
    tabular.append(customer_id)
    tabular.append(name)
    tabular.append(email)
    tabular.append(subscribed_status)
    with open(crm.DATAFILE, 'a') as file:
        file.write('\n')
        file.write(';'.join(tabular))
    list_customers()
   


def update_customer():
    element_list = data_manager.read_table_from_file(crm.DATAFILE)
    user_input = view.get_input('Please enter the id for the customer you want to update: ')
    for row in element_list:
        if user_input == row[ID_COLUMN]:
            name = view.get_input('Please enter a new name: ')
            email = view.get_input('Please enter a new email: ')
            subscribed_status = view.get_input('Please enter a subscribed status (1: yes, 0: no): ')
            row[NAME_COLUMN] = name
            row[EMAIL_COLUMN] = email
            row[SUBSCRIBED_COLUMN] = subscribed_status
            data_manager.write_table_to_file(crm.DATAFILE, element_list)
    list_customers()



def delete_customer():
    element_list = data_manager.read_table_from_file(crm.DATAFILE)
    user_input = view.get_input('Please enter the id for the customer you want to delete: ')
    for row in element_list:
        if user_input == row[ID_COLUMN]:
            removed_row = row
            print('Customer has been deleted from the database!')
            element_list.remove(removed_row)   
            data_manager.write_table_to_file(crm.DATAFILE, element_list)
    list_customers()
   


def get_subscribed_emails():
    emails = []
    element_list = data_manager.read_table_from_file(crm.DATAFILE)
    for row in element_list:
        if row[-1] == '1':
            emails.append(row[EMAIL_COLUMN])
    for email in emails:
        print(email, end='\n')



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
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
