# it is used for the fixure, when the fixture func is not found in the same file, it will come in this file and it will execute

import pytest

@pytest.fixture(scope="function")
def preSetupWork():
    print("this is from conftest file")
