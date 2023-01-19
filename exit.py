import sys
import project

def exit(messsage: str, code: int):
    project.print_space()
    print(f"{messsage}")
    sys.exit(int(code))