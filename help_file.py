import os
import exit
def get_latest_help_file():
    # https://realpython.com/working-with-files-in-python/#:~:text=To%20get%20a%20list%20of,scandir()%20in%20Python%203.
    folder = os.scandir("help/")
    list = []
    for file in folder:
        file1 = file.name
        if file1 == "help_file.txt":
            continue

        file1 = file1.replace("help_v", "").replace(".txt", "").replace("-", ".")

        try:
            file1 = float(file1)
        except:
            exit.exit("Server Naming Error", 1)
            pass
        list.append(file1)
    return f"help/help_v{str(max(list)).replace('.', '-')}.txt"
