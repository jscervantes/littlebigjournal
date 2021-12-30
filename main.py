#!/usr/bin/python3

import os
import sys
import datetime


#================ Creation/Deletion Functions ==================


def make_journal():
    print("========\n")
    name = input("Please input name of journal: ")

    cwd = os.getcwd()
    path = cwd + "/Journals/" + name 

    try:
        os.mkdir(path)
    except OSError: 
        print(f"Creation of the directory {path} failed.")
    else:
        print(f"Journal {path} successfully created.\n")


def delete_journal():
    main_cwd = os.getcwd()
    journal_list = os.listdir(main_cwd + "/Journals")
    print("\nJournals available for deletion:\n")
    for journal in journal_list:
        print('- '.rjust(5) + journal)

    journal = input("\nWhich Journal would you like to delete? ")
    path = main_cwd + "/Journals/" + journal

    try:
        os.rmdir(path)
    except OSError:
        print("\nJournal could not be deleted. You sure it exists?\n")
    else: print(f"Journal {journal} successfully deleted.")

def view_journals():
    main_cwd = os.getcwd()
    journal_list = os.listdir(main_cwd + "/Journals")
    
    print("\nJournals collected:\n")
    for journal in journal_list:
        print('- '.rjust(5) + journal)
    print()
    

#=============== Journal Editing Functions ===========================


def open_journal():
    while True:
        main_cwd = os.getcwd()
        journal_list = os.listdir(main_cwd + '/Journals')

        print("\nTotal Journals: " + str(len(journal_list)))
        if len(journal_list) < 1:
            print("There are no journals to open. Try creating one!")
            return

        print("Journals available:\n")
        for journal in journal_list:
            print('- '.rjust(5) + journal)
        print("\n========\n")

        name = input("Choose a journal to open: ")
        journal_path = main_cwd + '/Journals/' + name

        try:
            os.chdir(journal_path)
            print(f"\nJournal {name} opened.\n")
            break
        except OSError:
            print("Journal not found. You sure it exists?")

    entries_list = os.listdir('.')
    print("Current Entries: " + str(len(entries_list)) + "\n")
    for entry in entries_list:
        print(entry.rjust(15, '.'))
    print()

    while True:
        print("What would you like to do?")
        print("Enter 'help' for available commands.")
        print("=========\n")
        choice = input(">>> ")

        if choice == "help":
            print("\nJournal editing (Need to open journal first)")
            print("    add          Add entry to a journal")
            print("    delete       Remove entry from journal")
            print("    help         Opens this menu")
            print("    read         Read an entry")
            print("    close        Close current journal")
            print("    exit         Go back to real life")
            print("========\n")
            continue
        if choice == "add":
            opened_journal_entry(journal_path)
        elif choice == "delete":
            remove_entry()
        elif choice == "read":
            read_entry(journal_path)
        elif choice == "exit":
            print("Smell ya later...")
            sys.exit()
        elif choice == "close":
            os.chdir(main_cwd)
            return


def fetch_entry():
    print("Your entry: ")
    entry = input(">>>")
    return entry


def journal_entry():
    main_cwd = os.getcwd()
    journal_list = os.listdir(main_cwd + '/Journals')

    print("\nJournals available:\n")
    for journal in journal_list:
        print('- '.rjust(5) + journal)
    print("\nWhich journal would you like to add to?")
    print("========\n")

    journal = input(">>> ")
    
    if journal == "" or journal == "exit":
        return 
    else:
        title = input("\nTitle for this entry \
                (if left blank, date will be used): ")

    entry = fetch_entry()
    today = datetime.datetime.now()

    #======Entry formatting=======
    char_count = 0
    formatted_entry = "\n" + today.strftime("%H:%M:%S") + "\n"
    for i in entry:
        if char_count < 50:
            formatted_entry += i
            char_count += 1
        else:
            formatted_entry += '\n'
            char_count = 0
    formatted_entry += "\n"
    #=============================            

    if title == "":
        entry_file = open(main_cwd + '/Journals/' + journal \
                + '/' + today.strftime("%m_%d_%y") + '.txt', 'a')
    else:
        entry_file = open(main_cwd + '/Journals/' + journal \
                + '/' + title + '.txt', 'a')

    entry_file.write(formatted_entry)
    entry_file.close()
    print(f"\n~Entry added to {journal} successfully.~\n")
        

def opened_journal_entry(journal_path):
    title = input("Title for this entry (if left blank, date will be used): ")

    entry = fetch_entry()
    today = datetime.datetime.now()

    #======Entry formatting=======
    char_count = 0
    formatted_entry = "\n" + today.strftime("%H:%M:%S") + "\n"
    for i in entry:
        if char_count < 50:
            formatted_entry += i
            char_count += 1
        else:
            formatted_entry += '\n'
            char_count = 0
    formatted_entry += "\n"
    #=============================            

    if title == "":
        entry_file = open(journal_path + '/' + today.strftime("%m_%d_%y") \
                + '.txt', 'a')
    else:
        entry_file = open(journal_path + '/' + title + '.txt', 'a')

    entry_file.write(formatted_entry)
    entry_file.close()
    print(f"\n~Entry added to {os.path.basename(journal_path)} successfully.~\n")


def read_entry(journal_path):
    entries_list = os.listdir('.')
    print("Current Entries: " + str(len(entries_list)) + "\n")
    for entry in entries_list:
        print(entry.rjust(15, '.'))
        
    print("\nWhich entry would you like to read?\n")
    entry_selection = input(">>> ")
    
    try:
        entry_file = open(journal_path + '/' + entry_selection)
        entry_contents = entry_file.read()
        print("\n...\n")
        print("".rjust(5) + entry_contents)
        print("\n...\n")
    except OSError:
        print("\nI don't know if that entry exists...\n")


#def delete_entry():
    

def main():

    #========= Launch Graphic ============
    print("\nWelcome to...\n")
    print("=" * 44)
    for i in range(2):
        print("| |" + "".center(40) + "|")
    print("| |" + "________________".center(40) + "|")
    print("| |" + "| ~Bonjournal~ |".center(40) + "|")
    print("| |" + "----------------".center(40) + "|")
    for i in range(3):
        print("| |" + "".center(40) + "|")
    #=====================================

    print("\nEnter 'help' for available commands.")

    while True:
        print("\nWhat would you like to do?")
        print("========\n")
        choice = input(">>> ")

        if choice == "help":
            print("\nJournal creation and deletion")
            print("    create       Create a journal")
            print("    destroy      Delete a journal")
            print("    view         List journals available")
            print("    open         Open a journal")
            print("\nJournal editing (Need to open journal first)")
            print("    add          Add entry to a journal")
            print("    delete       Remove entry from journal")
            print("    help         Opens this menu")
            print("    exit         Go back to real life\n")
            continue
        elif choice == "create":
            make_journal()
        elif choice == "open":
            open_journal()
        elif choice == "destroy":
            delete_journal()
        elif choice == "view":
            view_journals()
        elif choice == "add":
            journal_entry()
        elif choice == "delete":
            remove_entry()
        elif choice == "exit":
            print("Until next time...")
            sys.exit()
        else:
            print("\nCommand not recognized. Enter 'help' if lost.")
            continue

        print("========\n")
        continue_choice = input("Anything else? y/n: ") 

        if continue_choice == "n" or continue_choice == "no":
            print("See ya...")
            return
        elif continue_choice == "y" or continue_choice == "yes":
            continue
        

if __name__ == "__main__":
    main()
