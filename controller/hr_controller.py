from model.hr import hr
from view import terminal as view
from model import data_manager
import datetime


def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_birth_date():
    dates_of_birth = []
    ages = []
    element_list = data_manager.read_table_from_file(hr.DATAFILE)
    for row in element_list:
        ages.append(row[2])
    for dob in ages:
        dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
        new_dob = from_dob_to_age(dob)
        dates_of_birth.append(new_dob)
    return dates_of_birth

def list_employees():
    view.print_error_message("Not implemented yet.")


def add_employee():
    view.print_error_message("Not implemented yet.")


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    names = []
    indexes = []
    element_list = data_manager.read_table_from_file(hr.DATAFILE)
    for row in element_list:
        names.append(row[1])
    dates_of_birth = get_birth_date()
    for dob in dates_of_birth:
        indexes.append(dates_of_birth.index(max(dates_of_birth)))
        indexes.append(dates_of_birth.index(min(dates_of_birth)))
    print(f'The oldest employee is {names[indexes[0]]} and youngest one is {names[indexes[1]]}')
    return (names[indexes[0]], names[indexes[1]])

    
def get_average_age():
    ages = get_birth_date()
    average_age = sum(ages)/len(ages)
    rounded_age = int(round(average_age))
    print(f'The average age of employees is {rounded_age}.')


def next_birthdays():
    birth_dates = []
    names = []
    indexes = []
    employees_with_birthdate_2_weeks = []
    date_input = input('Please enter a date (e.g. 2018-02-06): ')
    element_list = data_manager.read_table_from_file(hr.DATAFILE)
    start_date = datetime.datetime.strptime(date_input, '%Y-%m-%d')
    add_two_weeks = datetime.timedelta(days=14)

    end_date = start_date + add_two_weeks
    start_date = str(start_date)
    end_date = str(end_date)
    print(type(start_date))
    print(type(end_date))
    start_date = start_date[:-9]
    end_date = end_date[:-9]
    print(start_date)
    print(end_date)
    for row in element_list:
        birth_dates.append(row[2])
        names.append(row[1])
    for date in birth_dates:
        if start_date < date and date < end_date:
            indexes.append(birth_dates.index(date))
    for index in indexes:
        employees_with_birthdate_2_weeks.append(names[index])
    employeez = ''.join(employees_with_birthdate_2_weeks)
    print(f'The emoployees with birthdays between the {start_date} and the date after 2 weeks are: {employeez}')
        

def count_employees_with_clearance():
    employees = []
    element_list = data_manager.read_table_from_file(hr.DATAFILE)
    clearance_level = int(view.get_input('Please enter a clearance level: '))
    view.print_error_message("Not implemented yet.")
    for row in element_list:
        if  int(row[-1]) >= clearance_level:
            employees.append(1)
    print(f'The number of employees is: {len(employees)}')


def count_employees_per_department():

    element_list = data_manager.read_table_from_file(hr.DATAFILE)
    

def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
