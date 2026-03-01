def test_a1():
    assert 5+5 == 10
    assert 5-5 == 0
    assert 5*5 == 25
    assert 5/5 == 1
    assert 5**2 == 25

# def test_a2():
#     assert 10%3 == 10 #failing test
#     assert 10//3 == 3
#     assert 10%2 == 0
#     assert 10//2 == 5

def test_a3():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def test_a4():
    assert(3-1*4/2) == 2.0 #failing test, order of operations is not correct
    assert 'put' in 'notput' #failing test, 'put' is not in 'notputS'
