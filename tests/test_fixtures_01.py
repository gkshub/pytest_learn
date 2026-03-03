import pytest

@pytest.fixture(scope="module")
def setup_list():
    print("\n in fixture setup_list")
    city = ["Delhi", "Mumbai", "Bangalore", "Chennai"]
    return city

def test_case_01(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == "Delhi"
    assert setup_list[::] == ["Delhi", "Mumbai", "Bangalore", "Chennai"]
    assert setup_list[::1] == ["Delhi", "Mumbai", "Bangalore", "Chennai"]
    assert setup_list[::-1] == ["Chennai", "Bangalore", "Mumbai", "Delhi"]


@pytest.mark.fixture()
def test_demo():
    print("\n in test_demo")
    assert 2+3 == 5
