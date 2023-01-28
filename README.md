# Nitro Regexes
#### Video Demo: https://youtu.be/lmaPbr7xFL0
#### Description: A better way to test your regexs

Nitro Regexes is a simple Python Module to test your regexes. It doesn't require wifi and is pretty fast. You can import your files full of regexes.

## Introduction
I got this idea in week 7 when I was testing regexes by creating a test.py file and running it there. It was very tedious and I soon got sick of it. So in week 9, I implemented Nitro Regexes for my and other's use.

## project.py
In project.py there are 9 functions.
The mains ones are:
main() which is the main menu of the project

save() which is where you can save your regexes

test() is where you can test your regexes

delete() is where you can delete your regexes

help() is where it will display a help document to walk you through the process

Also:
print_space() is for printing spaces to create the illusion that the interface is changing

change() to change the file_path of the regexes file. It is very useful when importing other regexes

print_re() is a function to print all the regexes in the regexes file

test_file() to test if the file exists


## exit.py
In exit.py is an exit function there is a function that prints an exit message and exits the program.
I chose to make it into a defferent file because I can easily import it into other files


## help_file.py 
help_file.py is a simple program to retrieve the latest help files from the help folder. The reason we made this is so that we can still keep the earlier version of the help document but not change any code while saving a new one.


## test_project.py
In this file I implemented multiple Unit and Integration tests to test the correctness of the code in project.py

Other functions in it are:
read_file() to read and convert a file to a str

get_output() to get the output from the CLI so we can check it

clear_test_file() to clear the test_regex file

add_regex() to add a regex to the file by file writing

add_regexes_normal() a list of regexes to be added to a file

add_regexes_test() a list of testable regexs to be added to a file


## test_data
### test_files
In the test_files folder there is test_regex.txt, a sample regex file where we can check if the program is working or not. Used in test_project.py


### test_output
In test_output there are some folders. In each folder there will be multiple text files. The text files contain the output that I expect and the output that test_project can use to compare. The folder names correspond to the functions in project.py


## regex_data
In regex_data there are two files

### regex_path.txt
In this file we store the path to the regex file. Used in change()
I chose to do this because if the user accidentally entered an invalid file path, the user can manually change it in regex_path.txt

### regex.txt
regex.txt is the default location to store your regexes. I chose this because it is permanent.


## help
In the help folder there are help files.

A sample help file:
Welcome to the help page! This is help v1.2
Anything indented is from the terminal.
When you run python3 re_search.py, or python re_search.py, you will be brought to this menu:
     __  __                  
    |  \/  |                 
    | \  / | ___ _ __  _   _ 
    | |\/| |/ _ \ '_ \| | | |
    | |  | |  __/ | | | |_| |
    |_|  |_|\___|_| |_|\__,_|
                            
                            
        [1] Save New Regex
        [2] Delete Regexes
        [3] Test Regexes
        [4] Change File
        [5] Help
        [6] Quit
    $ 

Type one of the numbers specified and press enter. You whisked away to one of the 5 pages.
They are:
    1. Save New Regex
    2. Delete Regexes
    3. Test Regexes
    4. Change File
    5. Help

If you typed 1 and pressed enter,
You will be at this page:

     _____                 
    / ____|                
    | (___   __ ___   _____ 
     \___ \ / _` \ \ / / _ \
     ____) | (_| |\ V /  __/
    |_____/ \__,_| \_/ \___|
                            
                            
    You are in the Save Function.
    Type quit() at anytime to go back to the menu.
    Type add() to add a Regex.

    Regexes currently loaded:

    $ 

In this page you can save your regexes (or regular expressions)
Type add() and press enter to see this:

    Regex: 

Here you can specify your regex and press enter. Then you will see this:

    Are you sure you want to add this Regex? y/n: 

Type y to add the regex and type n to type in your regex again.
If you typed in N and pressed enter, you will see this:

    Regex: 

where you can enter your regex again.
If you typed in y and pressed enter, you will see this:

    Regex added successfully
    Regexes currently loaded:
    [0] testing

as testing being your regex.
You will now be reprompted to enter another regex:

    Regex:

You can enter quit() and press enter to get back to this:

    $ 

Where you can type quit() and press enter again to get back to the menu.
     __  __                  
    |  \/  |                 
    | \  / | ___ _ __  _   _ 
    | |\/| |/ _ \ '_ \| | | |
    | |  | |  __/ | | | |_| |
    |_|  |_|\___|_| |_|\__,_|
                            
                            
        [1] Save New Regex
        [2] Delete Regexes
        [3] Test Regexes
        [4] Change File
        [5] Help
        [6] Quit
    $ 

If you type 2 and pressed enter,
you will see this page:

     _____       _      _       
    |  __ \     | |    | |      
    | |  | | ___| | ___| |_ ___ 
    | |  | |/ _ \ |/ _ \ __/ _ \
    | |__| |  __/ |  __/ ||  __/
    |_____/ \___|_|\___|\__\___|
                                
                                
    You are in the Delete Function.
    Type quit() at anytime to go back to the menu.
    Type delete() to delete a Regex.
    Type delete_all() to delete all Regexes

    Regexes currently loaded:
    [0] testing
    [1] .*

    $ 
    
as under the Regexes currently loaded: are your regexes.
To delete a regex, type delete() and press enter. Then, you will see this:

    Regex index: 

This referrs to the numbers beside the regexes.
For e.g. 
    [0] testing
enter 0 to delete testing.

enter a regex index, then you will see this:

    Are you sure you want to delete this Regex? y/n: 

if you entered n, you can go back to entering your regex index,

    Regex index: 

but if you entered y, you will see this:

    Regex deleted successfully
    Regexes currently loaded:
    [0] .*

    $
Under Regexes currently loaded:, your regex that you deleted will be gone
You can now delete more regexes
if you enter delete_all(), you will see a confirmation message. If you accept that, akk your regexes will be deleted


If you enter quit(),
you will go back to the menu.

     __  __                  
    |  \/  |                 
    | \  / | ___ _ __  _   _ 
    | |\/| |/ _ \ '_ \| | | |
    | |  | |  __/ | | | |_| |
    |_|  |_|\___|_| |_|\__,_|
                            
                            
        [1] Save New Regex
        [2] Delete Regexes
        [3] Test Regexes
        [4] Change File
        [5] Help
        [6] Quit
    $ 

If you enter 3,
you will see this:

     _______        _   
    |__   __|      | |  
       | | ___  ___| |_ 
       | |/ _ \/ __| __|
       | |  __/\__ \ |_ 
       |_|\___||___/\__|
                    
                    
    You are in the Test Function.
    Type quit() at anytime to go back to the menu.
    Type test() to test a Regex.

    Regexes currently loaded:
    [0] testing
    [1] \w*

    $ 

as under Regexes currently loaded:
there are your regexes

if you enter test()
you will be prompted with a regex index.
Enter it like the delete section and you will see this:

    Type quit() to break out of this loop!
    Your current Regex: \w*
    Input: 

as Your current Regex being your current Regex that you choosen.
Now this program uses re.search to search, so you can input a value to use the re.search on.
The program will return true or false.

if you enter quit(), you will see this:
    
    Regex index: 

if you enter quit() again,
you will see this:

    Regex tested successfully
    Regexes currently loaded:
    [0] testing
    [1] \w*


If you enter quit again, you will get to the menu page
if you enter 4 you will see this:

      _____ _                              ______ _ _      
     / ____| |                            |  ____(_) |     
    | |    | |__   __ _ _ __   __ _  ___  | |__   _| | ___ 
    | |    | '_ \ / _` | '_ \ / _` |/ _ \ |  __| | | |/ _ \
    | |____| | | | (_| | | | | (_| |  __/ | |    | | |  __/
     \_____|_| |_|\__,_|_| |_|\__, |\___| |_|    |_|_|\___|
                               __/ |                       
                              |___/                        
    Path to new file: 

The regex files are stored in the regex_data folder. in the regex_data folder, you can see regex.txt with your regexes.
you can edit regex.txt manually to get regexes as well.

You can make a new file or import a .txt file with regexes in rows, where each regex is a line.
Enter in the path to your new file and you will get back to the menu.

IMPORTANT: If you import another file other than a txt file, your program will crash everytime you run it. To fix the file error, go to regex_path.txt in the regex_data directory
and edit the path.

If you entered anything else your program will interpret it as you exiting the program.
Thank you for reading,
Bye
