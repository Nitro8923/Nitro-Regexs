# https://stackoverflow.com/questions/39506572/how-to-test-function-that-has-two-or-more-inputs-inside
# https://www.youtube.com/watch?v=dN-pVt7i4Us

import project
import exit
import pytest

file_path = "test_data/test_files/test_regex.txt"

# class TestSave:
def test_save_function(mocker, capsys):
    mocker.patch('builtins.input', side_effect=["add()", "testing", "y"])
    project.save(file_path)
    stdout, stderr = capsys.readouterr()
    print(stdout)

