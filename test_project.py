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

def add_regex(regex, mocker):
    try:
        mocker.patch('builtins.input', side_effect=["add()", f"{regex}", "y"])
        project.save(file_path)
    except:
        pass



class TestSave:
    def test_save(self, mocker, capsys):
        clear_test_file()
            try:
                project.save(file_path)
            except:
                pass
            assert get_output(capsys) == read_file(f"{test_output_path}save/save0.txt")

        try:
            mocker.patch('builtins.input', side_effect=["add()"])
            project.save(file_path)
        except:
            pass
        assert get_output(capsys) == read_file(f"{test_output_path}save/save1.txt")

        try:
            mocker.patch('builtins.input', side_effect=["add()", "testing", "n"])
            project.save(file_path)
        except:
            pass
        assert get_output(capsys) == read_file(f"{test_output_path}save/save2.txt")

        try:
            mocker.patch('builtins.input', side_effect=["add()", "quit()"])
            project.save(file_path)
        except:
            pass
        assert get_output(capsys) == read_file(f"{test_output_path}save/save3.txt")

        try:
            mocker.patch('builtins.input', side_effect=["add()", "testing", "y"])
            project.save(file_path)
        except:
            pass
        assert get_output(capsys) == read_file(f"{test_output_path}save/save4.txt")

        clear_test_file()
