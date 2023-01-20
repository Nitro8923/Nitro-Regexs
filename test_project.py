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

def clear_test_file(file_path):
    with open(file_path, "w") as file:
        file.write("")

# todo    
def add_regex(file_path, regex):
    with open(file_path, "a") as file:
        file.write(f"{regex}\n")

def add_regexs_normal(file_path):
    clear_test_file(file_path)
    for i in [r"testing", r"testing1", r"foo", r"bar", r"baz"]:
        add_regex(file_path, i)

def add_regexs_test(file_path):
    clear_test_file(file_path)
    for i in [r"\w+", r".*", r"\w\w\d"]:
        add_regex(file_path, i)


# Unit Tests
class TestUnits:
    def test_save(self, mocker, capsys):
        clear_test_file(file_path)
        side_effects = [[], ["add()"], ["add()", "testing", "n"], ["add()", "quit()"], ["add()", "testing", "y"]]
        for i in range(len(side_effects)):
            try:
                mocker.patch("builtins.input", side_effect=side_effects[i])
                project.save(file_path)
            except StopIteration:
                pass
            assert get_output(capsys) == read_file(f"{test_output_path}save/save{i}.txt")
        clear_test_file(file_path)

    
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
            add_regexs_normal(file_path)
            try:
                mocker.patch("builtins.input", side_effect=side_effects[i])
                project.delete(file_path)
            except StopIteration:
                pass
            assert get_output(capsys) == read_file(f"{test_output_path}delete/delete{i}.txt")
        clear_test_file(file_path)
    

    def test_delete_all(self, mocker):
        add_regexs_normal(file_path)
        try:
            mocker.patch("builtins.input", side_effect=["delete_all()", "y"])
            project.delete(file_path)
        except StopIteration:
            pass
        with open(file_path) as file:
            if not file.read() == "":
                clear_test_file(file_path)
                raise AssertionError
        clear_test_file(file_path)

    def test_test(self, mocker, capsys):
        side_effects = [
            [],
            ["test()"],
            ["test()", "0", "hello", "---", "quit()", "quit()"],
            ["test()", "1", "quit()", "quit()"],
            ["test()", "2", "hh3", "hhd", "quit()", "quit()"]
        ]
        for i in range(len(side_effects)):
            add_regexs_test(file_path)
            try:
                mocker.patch("builtins.input", side_effect=side_effects[i])
                project.test(file_path)
            except StopIteration:
                pass
            assert get_output(capsys) == read_file(f"{test_output_path}test/test{i}.txt")
        clear_test_file(file_path)

    def test_change(self, mocker):
        add_regexs_normal("test_data/test_files/test_regex1.txt")
        add_regex("test_data/test_files/test_regex1.txt", "test")
        try:
            mocker.patch("builtins.input", side_effect=["test_data/test_files/test_regex1.txt"])
            project.change(file_path)
        except StopIteration:
            pass

        with open("regex_data/regex_path.txt", "r") as file:
            if not file.read() == "test_data/test_files/test_regex1.txt":
                raise AssertionError
        
        clear_test_file("test_data/test_files/test_regex1.txt")

        with open("regex_data/regex_path.txt", "w") as file:
            file.write("")
            file.write("regex_data/regex.txt")

class TestIntegration:
    def test_add_delete_integration(self, mocker):
        try:
            mocker.patch("builtins.input", side_effect=["add()", "testing", "y", "add()", "foo", "y", "add()", "bar", "y"])
            project.save(file_path)
        except StopIteration:
            pass

        with open(file_path) as file:
            if not file.read() == "testing\nfoo\nbar":
                clear_test_file(file_path)
                raise AssertionError
        
        try:
            mocker.patch("builtins.input", side_effect=["delete()", "0", "y", "delete()", "1", "y"])
            project.delete(file_path)
        except StopIteration:
            pass

        with open(file_path) as file:
            if not file.read() == "foo":
                clear_test_file(file_path)
                raise AssertionError

        clear_test_file(file_path)