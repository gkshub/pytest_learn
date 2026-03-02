
import string
import pytest
pytestmark = [pytest.mark.smoke]

# Markers in pytest are used to 
# categorize tests, 
# control test execution, 
# and provide additional metadata about the tests. 
# They allow you to group tests together, s
# kip certain tests under specific conditions, 
# or even run only a subset of tests based on the markers assigned to them. 
# Here are some common uses of markers in pytest:

@pytest.mark.sanity
def test_case_01():
    NUM= 9/4
    assert str(NUM) == "2.25"

@pytest.mark.sanity
def test_case_02():
    letter  =string.ascii_lowercase
    assert len(letter) == 26

@pytest.mark.sanity
@pytest.mark.stringtest
def test_case_03():
    s1 = "Python, pyest and automation"
    assert s1.split() == ['Python,', 'pyest', 'and', 'automation']
    assert s1.split(',') == ['Python', ' pyest and automation']


