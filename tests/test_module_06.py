import string
import pytest



def test_case_strjoin():
    s1 = "Python, pyest and automation"
    l1 = ['Python,', 'pyest', 'and', 'automation']
    l2 = ['Python', ' pyest and automation']
    assert ' '.join(l1) == s1

@pytest.mark.xfail
def test_case_str02():
    letters = string.ascii_lowercase
    assert len(letters) == 26

def test_case_str03():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'

