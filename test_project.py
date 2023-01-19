# https://stackoverflow.com/questions/39506572/how-to-test-function-that-has-two-or-more-inputs-inside
# https://www.youtube.com/watch?v=dN-pVt7i4Us

import project
import exit

class Input:

    def __init__(self, *args):
        self.args = iter(args) 

    def __call__(self, x):
        try:
            return next(self.args)
        except StopIteration:
            raise Exception("No more input")

file_path = "test_data/test_files/test_regex.txt"

class TestSave:
    def test_save_function(self, capsys):
        project.input = Input("add()")
        project.save(file_path)
        capsys.out.strip() == "Regex:"
