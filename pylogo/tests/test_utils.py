import os
import pytest
from pylogo.utils import log_call_stack, delete_files_with_extensions

def test_log_call_stack(tmpdir):
    file_path = os.path.join(tmpdir, "function_calls.log")

    @log_call_stack(file_path)
    def add(a, b, c):
        return a + b + c

    result = add(1, 2, 3)

    assert result == 6
    assert os.path.exists(file_path)

    with open(file_path, 'r') as file:
        assert "add - Arguments: 1, 2, 3" in file.read()


def test_delete_files_with_extensions(tmpdir):
    directory = tmpdir.mkdir("test_dir")
    file1 = directory.join("file1.csv")
    file2 = directory.join("file2.txt")
    file3 = directory.join("file3.csv")
    file4 = directory.join("file4.xlsx")

    file1.write("test")
    file2.write("test")
    file3.write("test")
    file4.write("test")

    extensions = [".csv", ".xlsx"]
    delete_files_with_extensions(str(directory), extensions)

    assert not os.path.exists(str(file1))
    assert os.path.exists(str(file2))
    assert not os.path.exists(str(file3))
    assert not os.path.exists(str(file4))

