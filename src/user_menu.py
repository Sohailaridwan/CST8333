__author__      = "Sohaila Ridwan"
__date__   = "April 14, 2018"


import os
import sys
from dataset import *
from db_meta import *
from db_crud import *

table_dict = {'1': 'categories', '2': 'geocodes', '3': 'priceindex'}
table_count = table_dict.__sizeof__()

def print_level1_menu():
    print("\n----------------------")
    print("----- MAIN MENU ------")
    print("----------------------")
    print("1. Create Database (takes some time)")
    print("2. View Existing Schema")
    print("3. CRUD Operation")
    print("4. Exit")


def print_level2_crud_menu():
    local_loop = True
    while local_loop:
        print("\n----------------------------------")
        print("----- SELECT CRUD OPERATION ------")
        print("----------------------------------")
        print("1. View Record")
        print("2. Insert Record")
        print("3. Edit Record")
        print("4. Delete Record")
        print("5. Back")

        local_choice = input("Enter your choice [1-5]: ")
        if local_choice == '1':
            ch = print_level3_table_menu()
            if int(ch) <= table_count:
                read_from_table(table_dict[ch])
        elif local_choice == '2':
            ch = print_level3_table_menu()
            if int(ch) < 4:
                add_new_record(table_dict[ch])
        elif local_choice == '3':
            ch = print_level3_table_menu()
            if int(ch) < 4:
                show_primary_key(table_dict[ch])
        elif local_choice == '4':
            ch = print_level3_table_menu()
            if int(ch) < 4:
                show_primary_key(table_dict[ch])
        elif local_choice == '5':
            print("Returning to parent menu.")
            return
        else:
            print("Invalid menu selection. Exiting program.")
            sys.exit()


def print_level2_schema_menu():
    local_loop = True
    while local_loop:
        print("\n-------------------------------")
        print("----- SELECT SCHEMA META ------")
        print("-------------------------------")
        print("1. View Table Names")
        print("2. View Table Description")
        print("3. View Table Primary Key")
        print("4. Back")

        local_choice = input("Enter your choice [1-4]: ")
        if local_choice == '1':
            show_tables()
        elif local_choice == '2':
            ch = print_level3_table_menu()
            if int(ch) < 4:
                show_table_desc(table_dict[ch])
        elif local_choice == '3':
            ch = print_level3_table_menu()
            if int(ch) < 4:
                show_primary_key(table_dict[ch])
        elif local_choice == '4':
            print("Returning to parent menu.")
            return
        else:
            print("Invalid menu selection. Exiting program.")
            sys.exit()


def print_level3_table_menu():
    menu = ('1', '2', '3', '4')
    print("\n------------------------------")
    print("----- SELECT TABLE NAME ------")
    print("------------------------------")
    print("1. Categories")
    print("2. Geocodes")
    print("3. Priceindex")
    print("4. Back")

    local_choice = input("Enter your choice [1-4]: ")

    if local_choice in menu:
        return local_choice
    else:
        print("Invalid menu selection. Exiting program.")
        sys.exit()

if __name__ == '__main__':
    loop = True
    while loop:
        print_level1_menu()
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            print("Creating Database")
        elif choice == '2':
            print_level2_schema_menu()
        elif choice == '3':
            print_level2_crud_menu()
        elif choice == '4':
            print("Exit")
            loop = False
        else:
            input("Invalid menu selection. Exiting program.")
            loop = False


