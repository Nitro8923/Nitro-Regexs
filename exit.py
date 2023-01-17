import sys
import re_search

def exit(messsage: str, code: int):
    re_search.print_space()
    print(f"{messsage}")
    sys.exit(int(code))