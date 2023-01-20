import re
import exit
import os
import help_file
from pyfiglet import Figlet
import sys

def main():
    print_space()
    # https://www.w3schools.com/python/python_variables_global.asp
    global figlet
    # https://github.com/pwaller/pyfiglet
    figlet = Figlet(font='big')
    with open("regex_data/regex_path.txt", "r") as file:
        regex_file = file.readline()

    while True:
        figlet = Figlet(font='big')
        print(figlet.renderText("Menu"), end="")
        print("    [1] Save New Regex\n    [2] Delete Regexes\n    [3] Test Regexes\n    [4] Change File\n    [5] Help\n    [6] Quit")
        
        
        
        if test_file(regex_file) == False:
            exit.exit(f"{regex_file} doesn't exists", 1)
        print("$ ", end="")
        value = input()
        if value == "1":
            save(regex_file)
        elif value == "2":
            delete(regex_file)
        elif value == "3":
            test(regex_file)
        elif value == "4":
            regex_file = change(regex_file) 
        elif value == "5":
            help()
        else:
            exit.exit("User Exit", 0)
        

def save(regex_file):
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Save"), end="")
    print("You are in the Save Function.\nType quit() at anytime to go back to the menu.\nType add() to add a Regex.\n")
    print_re(regex_file)
    while True:
        print("$ ", end="")
        value = input()
        if value == "add()":
            while True:
                print("Regex: ", end="")
                new_re = input()
                if new_re == "quit()":
                    break1 = True
                    break
                while True:
                    print("Are you sure you want to add this Regex? y/n: ", end="")
                    confirmation = input()
                    if confirmation.lower() == "y" or confirmation.lower() == "n":
                        break
                if confirmation.lower() == "y":
                    with open(regex_file, "a") as file:
                        file.write(f"{new_re}\n")
                    
                    print("Regex added successfully")
                    print_re(regex_file)
                    break
        elif value == "quit()":
            break 
    print_space()

def delete(regex_file):
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Delete"), end="")
    print("You are in the Delete Function.\nType quit() at anytime to go back to the menu.\nType delete() to delete a Regex.\nType delete_all() to delete all Regexes\n")
    print_re(regex_file)
    while True:
        print("$ ", end="")
        value = input()
        if value == "delete()":
            while True:
                print("Regex index: ", end="")
                re_index = input()
                if re_index == "quit()":
                    break
                if not re_index.isdigit():
                    continue
                while True:
                    print("Are you sure you want to delete this Regex? y/n: ", end="")
                    confirmation = input()
                    if confirmation.lower() == "y" or confirmation.lower() == "n":
                        break
                if confirmation.lower() == "y":
                    lines = []
                    with open(regex_file, 'r') as file:
                        lines = file.readlines()

                    # Src: https://pynative.com/python-delete-lines-from-file/
                    with open(regex_file, 'w') as file:
                        for number, line in enumerate(lines):
                            if number not in [int(re_index)]:
                                file.write(line)
                    
                    print("Regex deleted successfully")
                    print_re(regex_file)
                    break
            
            
        elif value == "delete_all()":
            while True:
                print("Are you sure you want to delete all Regexes? y/n: ", end="")
                confirmation = input()
                if confirmation.lower() == "y" or confirmation.lower() == "n":
                    break
            if confirmation.lower() == "y":
                with open(regex_file, 'w') as file:
                    file.write("")
                break
        elif value == "quit()":
            break
    print_space()

def test(regex_file):
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Test"), end="")
    print("You are in the Test Function.\nType quit() at anytime to go back to the menu.\nType test() to test a Regex.\n")
    print_re(regex_file)
    while True:
        print("$ ", end="")
        value = input()
        if value == "test()":
            while True:
                print("Regex index: ", end="")
                re_index = input()
                if re_index == "quit()":
                    break
                if not re_index.isdigit():
                    continue
                print("Type quit() to break out of this loop!")
                lines = []
                with open(regex_file, 'r') as file:
                    lines = file.readlines()

                # Src: https://stackoverflow.com/questions/6930982/how-to-use-a-variable-inside-a-regular-expression
                try:
                    re_string = lines[int(re_index)].replace("\n", "")
                except IndexError:
                    continue
                
                while True:
                    print(f"Your current Regex: {re_string}")
                    print("Input: ", end="")
                    value = input()
                    if value == "quit()":
                        break
                    try:
                        if re.search(r"{}".format(re_string), value):
                            print("True")
                        else:
                            print("False")
                    except:
                        print("There was a problem")
                        break
                print("Regex tested successfully")
                print_re(regex_file)
        elif value == "quit()":
            break 
    print_space()

def change(regex_file):
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Change File"), end="")
    # https://www.simplilearn.com/tutorials/python-tutorial/global-variable-in-python#:~:text=Use%20a%20global%20keyword%20to%20change%20the%20value,global%20variable%20inside%20the%20function.
    while True:
        print("Path to new file: ", end="")
        regex_file = input()
        if test_file(regex_file):
            break
    with open("regex_data/regex_path.txt", "w") as file:
        file.write(regex_file)
    print_space()
    return regex_file

def help():
    print_space()
    figlet = Figlet(font="big")
    print(figlet.renderText("Help"), end="")
    print("\n" * 20)
    with open(help_file.get_latest_help_file(), "r") as help_file_txt:
        print(help_file_txt.read())
    
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nScroll up to the top")
    print("Press enter at anytime to exit")
    input()
    print_space()

def print_re(regex_file):
    print("Regexes currently loaded:")
    list = []
    with open(regex_file, "r") as file:
        reader = file.readlines()
        i = 0
        for row in reader:
            list.append(f"[{i}] {row}")
            i += 1
    for row in list:
        print(row, end="")
    print()

def test_file(regex_file):
    if not os.path.exists(regex_file):
        return False
    list = []
    with open(regex_file, "r") as file:
        list.append(file.read())
    return True
    

def print_space():
    for _ in range(100):
        print()

if __name__ == "__main__":
    main()