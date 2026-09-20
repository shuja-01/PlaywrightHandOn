# pyrefly: ignore [missing-import]
from _pytest import cacheprovider
import pytest

# scope="function" : it will run for every test
# scope="class" : it will run once per class
# scope="module" : it will run once per module
# scope="session" : it will run once per session
# scope="package" : it will run once per package
@pytest.fixture(scope="function")
def prework():
    print("this is the starting")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("this is the starting")
    yield #this act as seprator between setup and tear down, firstly setup will execute, then yield{means go to test and then return} will execute and then tear down will execute
    print("tear down validation")


# passing "prework" as a parameter ensures that the fixture is run before the test
@pytest.mark.smoke
def test_initialCheck(prework, secondWork):
    print("THis is first test")
    # assert prework == "fail"
    assert prework == "pass"

@pytest.mark.smoke
def test_secondCheck(prework, secondWork):
    print("THis is second test")


print("test runned successfully")
