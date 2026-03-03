import pytest

weekdays1 = ["Monday", "Tuesday", "Wednesday"]
weekdays2 = ["Friday", "Saturday", "Sunday"]

@pytest.fixture()
def setup_01():
    wk1 = weekdays1.copy()
    wk1.append("Thursday")
    yield wk1
    print("\n in yield of setup_01")
    # wk1.clear()
    wk1.pop()

@pytest.fixture()
def setup_02():
    wk2 = weekdays2.copy()
    wk2.insert(0, "Thursday")
    yield wk2
    print("\n in yield of setup_02")

def test_case_01(setup_01):
    print("\n in test_case_01")
    print(setup_01)
    setup_01.extend(weekdays2)
    assert setup_01 == ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

def test_case_02(setup_01, setup_02):
    print("\n in test_case_02")
    assert len(weekdays1 + setup_02) == len(weekdays1 + setup_02)