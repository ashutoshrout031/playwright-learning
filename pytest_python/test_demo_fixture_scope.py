
# scope="function" fixture will be called before every test function executes

# scope="module" fixture will be called only once before test functions executes

# scope="class" fixture will be called only once before the class

# scope="session" fixture will be called only once for session


import pytest

# @pytest.fixture  # make the respective function as fixture function
# def setup(scope = "module"):  #default scope is function
#     print("setup browser...")

# If You want to run fixture method/function to be run before test method then you need to pass fixute method name as parameter in test method.
# def test_one(setup):
#     print("This is test one")

# def test_two():
#     print("This is test two")

# def test_three(setup):
#     print("This is test three")
        
# def test_four():
#     assert 1+1 ==2


# Fixture Return
# @pytest.fixture 
# def setup():
#     print("setup browser...")
#     return 3

# def test_four(setup):
#     assert setup == 2


# Yield 
@pytest.fixture 
def setup():
    print("setup browser...")
    yield
    print("Closes browser")


def test_one(setup):
    print("This is test one")

def test_two(setup):
    print("This is test two")

def test_three(setup):
    print("This is test three")
        
def test_four(setup):
    assert 1+1 ==2

# Entry -----> test_function -----> Yield

