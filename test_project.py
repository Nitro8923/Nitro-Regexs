# https://stackoverflow.com/questions/39506572/how-to-test-function-that-has-two-or-more-inputs-inside
# https://www.youtube.com/watch?v=dN-pVt7i4Us

import project
import exit
import pytest

file_path = "test_data/test_files/test_regex.txt"

test_output_path = "test_data/test_output/"

def read_file(file):
    with open(file) as file:
        return file.read().replace("\n", "")

def get_output(capsys):
    stdout, stderr = capsys.readouterr()
    return stdout.replace("\n", "")

def clear_test_file():
    with open("test_data/test_files/test_regex.txt", "w") as file:
        file.write("")

# todo
def add_regexs(file_path, regex):


def add_regexs_delete(file_path):
    clear_test_file()
    with open(file_path, "a") as file:
        for i in ["testing", "testing1", "foo", "bar", "baz"]:
            file.write(f"{i}\n")

def add_regexs_test(file_path)


# Unit Tests
class TestUnits:
    def test_save(self, mocker, capsys):
        clear_test_file()
        side_effects = [[], ["add()"], ["add()", "testing", "n"], ["add()", "quit()"], ["add()", "testing", "y"]]
        for i in range(len(side_effects)):
            try:
                mocker.patch('builtins.input', side_effect=side_effects[i])
                project.save(file_path)
            except StopIteration:
                pass
            assert get_output(capsys) == read_file(f"{test_output_path}save/save{i}.txt")
        clear_test_file()

    
    def test_delete(self, mocker, capsys):
        side_effects = [
            [], 
            ["delete()"], 
            ["delete()", "1", "n"], 
            ["delete()", "quit()"], 
            ["delete()", "1", "y"], 
            ["delete_all()", "n"],
        ]
        for i in range(len(side_effects)):
            add_regexs(file_path)
            try:
                mocker.patch("builtins.input", side_effect=side_effects[i])
                project.delete(file_path)
            except StopIteration:
                pass
            assert get_output(capsys) == read_file(f"{test_output_path}delete/delete{i}.txt")
    

    def test_delete_all(self, mocker):
        try:
            mocker.patch("builtins.input", side_effect=["delete_all()", "y"])
            project.delete(file_path)
        except:
            pass
        with open(file_path) as file:
            if not file.read() == "":
                raise AssertionError
    
    
