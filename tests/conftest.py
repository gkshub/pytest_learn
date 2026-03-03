import pytest

def pytest_configure():
    pytest.weekdays1 = ["Monday", "Tuesday", "Wednesday"]
    pytest.weekdays2 = ["Friday", "Saturday", "Sunday"]

@pytest.fixture()
def setup_01():
    wk1 = pytest.weekdays1.copy()
    wk1.append("Thursday")
    yield wk1
    print("\n in yield of setup_01")
    # wk1.clear()
    wk1.pop()

@pytest.fixture()
def setup_02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "Thursday")
    yield wk2
    print("\n in yield of setup_02")