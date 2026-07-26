# Fixture : Normal Re-usable function (Not Test Function)

import pytest

@pytest.fixture  # make the respective function as fixture function
def setup():
    print("setup browser...")

# If You want to run fixture method/function to be run before test method then you need to pass fixute method name as parameter in test method.
def test_one(setup):
    print("This is test one")

def test_two():
    print("This is test two")

def test_three(setup):
    print("This is test three")
        
def test_four():
    assert 1+1 ==2
