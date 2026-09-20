# pyrefly: ignore [missing-import]
import pytest

@pytest.mark.smoke
def test_thirdCheck(preSetupWork):
    print("THis is second test")


print("test runned successfully")
