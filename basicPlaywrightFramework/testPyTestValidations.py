# pyrefly: ignore [missing-import]
import pytest

# scope="function" : it will run for every test
# scope="class" : it will run once per class
# scope="module" : it will run once per module
# scope="session" : it will run once per session
# scope="package" : it will run once per package
@pytest.fixture(scope="function")
def prework():
    print("this is the starting")

# passing "prework" as a parameter ensures that the fixture is run before the test
def test_initialCheck(prework):
    print("THis is first test")


print("test runned successfully")