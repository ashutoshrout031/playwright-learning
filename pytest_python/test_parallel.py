'''
Required plugin - pytest-xdist

'''


def test_one():
    print("rinning test one")
    assert True

def test_two():
    print("rinning test two")
    assert True

def test_three():
    print("rinning test three")
    assert True

def test_four():
    print("rinning test four")
    assert True

# pytest pytest_python\test_parallel.py -s -v -n 2    -n no of workers max 5 otherwise it will slow