import io
import os
import sys
import unittest
from unittest.mock import patch
from script import find_files

current_dir = os.path.dirname(__file__)
test_root_dir = os.path.join(current_dir, 'test-dir')
test_user_input = '[a-z]+ample'
expected_output = "{'.': 0, 'a': 1, 'a/b': 2, 'a/b/c': 3, 'd': 2, 'd/e': 0, 'd/e/f': 2}\n"

class Find_Files(unittest.TestCase):

    @patch('script.get_root_dir', return_value=test_root_dir)
    @patch('script.get_user_input', return_value=test_user_input)
    def test_dict_generation(self,root_dir, user_input):
        capture_output = io.StringIO()
        sys.stdout = capture_output
        find_files()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue() , expected_output)

if __name__ == '__main__':
    unittest.main()
