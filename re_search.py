import re
import exit
import os
from pyfiglet import Figlet

def main():
    print_space()
    # https://www.w3schools.com/python/python_variables_global.asp
    global FILE
    global figlet
    # https://github.com/pwaller/pyfiglet
    figlet = Figlet(font='big')
    while True:
        figlet = Figlet(font='big')
        print(figlet.renderText("Menu"), end="")
        print("    [1] Save New Regex\n    [2] Delete Regexs\n    [3] Test Regexs\n    [4] Change File\n    [5] Quit")
        
        with open("file.txt", "r") as file:
            FILE = file.readline()
        if test_file() == False:
            exit.exit(f"{FILE} doesn't exists", 1)
        value = input("$ ")
        if value == "1":
            save()
        elif value == "2":
            delete()
        elif value == "3":
            test()
        elif value == "4":
            change()
            

        else:
            exit.exit("User Exit", 0)
        

def save():
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Save"), end="")
    print("You are in the Save Function.\nType quit() at anytime to go back to the menu.\nType add() to add a Regex.\n")
    print_re()
    while True:
        value = input("$ ")
        if value == "add()":
            while True:
                new_re = input("Regex: ")
                if new_re == "quit()":
                    break
                while True:
                    confirmation = input("Are you sure you want to add this Regex? y/n: ")
                    if confirmation.lower() == "y" or confirmation.lower() == "n":
                        break
                if confirmation.lower() == "y":
                    break
            
            with open(FILE, "a") as file:
                file.write(f"{new_re}\n")
            
            print("Regex added successfully")
            print_re()
        elif value == "quit()":
            break 
    print_space()

def delete():
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Delete"), end="")
    print("You are in the Delete Function.\nType quit() at anytime to go back to the menu.\nType delete() to delete a Regex.\nType delete_all() to delete all Regexs\n")
    print_re()
    while True:
        value = input("$ ")
        if value == "delete()":
            while True:
                re_index = input("Regex index: ")
                if re_index == "quit()":
                    break
                if not re_index.isdigit():
                    continue
                while True:
                    confirmation = input("Are you sure you want to delete this Regex? y/n: ")
                    if confirmation.lower() == "y" or confirmation.lower() == "n":
                        break
                if confirmation.lower() == "y":
                    break
            
            lines = []
            with open(FILE, 'r') as file:
                lines = file.readlines()

            # Src: https://pynative.com/python-delete-lines-from-file/
            with open(FILE, 'w') as file:
                for number, line in enumerate(lines):
                    if number not in [int(re_index)]:
                        file.write(line)
            
            print("Regex deleted successfully")
            print_re()
        elif value == "delete_all()":
            while True:
                confirmation = input("Are you sure you want to delete all Regexs? y/n: ")
                if confirmation.lower() == "y" or confirmation.lower() == "n":
                    break
            if confirmation.lower() == "y":
                with open(FILE, 'w') as file:
                    file.write("")
                break
        elif value == "quit()":
            break
    print_space()

def test():
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Test"), end="")
    print("You are in the Test Function.\nType quit() at anytime to go back to the menu.\nType test() to test a Regex.\n")
    print_re()
    while True:
        value = input("$ ")
        if value == "test()":
            while True:
                re_index = input("Regex index: ")
                if re_index == "quit()":
                    break
                if not re_index.isdigit():
                    continue
                print("Type quit() to break out of this loop!")
                lines = []
                with open(FILE, 'r') as file:
                    lines = file.readlines()

                # Src: https://stackoverflow.com/questions/6930982/how-to-use-a-variable-inside-a-regular-expression
                re_string = lines[int(re_index)].replace("\n", "")
                re_string = r"{}".format(re_string)
                
                while True:
                    print(f"Your current Regex: {re_string}")
                    value = input("Input: ")
                    if value == "quit()":
                        break
                    try:
                        if re.search(f"{re_string}", value):
                            print("True")
                        else:
                            print("False")
                    except:
                        print("There was a problem")
                        break
            
            print("Regex tested successfully")
            print_re()
        elif value == "quit()":
            break 
    print_space()

def change():
    print_space()
    figlet = Figlet(font='big')
    print(figlet.renderText("Change File"), end="")
    # https://www.simplilearn.com/tutorials/python-tutorial/global-variable-in-python#:~:text=Use%20a%20global%20keyword%20to%20change%20the%20value,global%20variable%20inside%20the%20function.
    global FILE 
    while True:
        FILE = input("Path to new file: ")
        if test_file():
            break
    with open("file.txt", "w") as file:
        file.write(FILE)
    print_space()

def print_re():
    print("Regexs currently loaded:")
    list = []
    with open(FILE, "r") as file:
        reader = file.readlines()
        i = 0
        for row in reader:
            list.append(f"[{i}] {row}")
            i += 1
    for row in list:
        print(row, end="")
    print()

def test_file():
    if not os.path.exists(FILE):
        return False
    return True
    

def print_space():
    for _ in range(100):
        print()

if __name__ == "__main__":
    main()