import pytest

def test_loginByEmail():
    print("this is login by email test")
    assert 1==1

def test_loginByFacebook():
    print("this is login by facebook test")
    assert 1==1
@pytest.mark.skip  # Skip the test method
def test_loginByPhone():
    print("this is login by phone test")
    assert 1==1

def test_signupByEmail():
    print("this is signup by email test")
    assert True == True

@pytest.mark.skip
def test_signupByFacebook():
    print("this is signup by facebook test")
    assert True == True

def test_signupByPhone():
    print("this is signup by phone test")
    assert True == True