'''
grouping tests:

test_LoginByEmail -> sanity, regression
test_LoginByFacebook -> sanity
test_LoginByPhone -> regression
test_signupByEmail -> sanity, regression
test_signupByFacebook -> regression
test_signupbyphone -> sanity
test_paymentindollor -> sanity, regression
test_paymentinrupees -> regression

'''
# The groups are user defined

import pytest


@pytest.mark.sanity
@pytest.mark.regression 
def test_loginByEmail():
    print("this is login by email test")
    assert 1==1
@pytest.mark.sanity
def test_loginByFacebook():
    print("this is login by facebook test")
    assert 1==1
@pytest.mark.regression 
def test_loginByPhone():
    print("this is login by phone test")
    assert 1==1
@pytest.mark.sanity
@pytest.mark.regression 
def test_signupByEmail():
    print("this is signup by email test")
    assert True == True

@pytest.mark.regression
def test_signupByFacebook():
    print("this is signup by facebook test")
    assert True == True


@pytest.mark.sanity
def test_signupByPhone():
    print("this is signup by phone test")
    assert True == True

@pytest.mark.sanity
@pytest.mark.regression
def test_paymentInDollar():
    print("this is payment in dollar test")
    assert 1 == 1

@pytest.mark.regression
def test_paymentInRupees():
    print("this is payment in ruppees test")
    assert 1 == 1



# to run specific tests then 
'''
1> Run Sanity test ----> pytest pytest_python\test_grouping.py -v -s -m "sanity"
2> Run only Regression -----> pytest pytest_python\test_grouping.py -v -s -m "regression"
3> Run both sanity and regression -----> pytest pytest_python\test_grouping.py -v -s -m "sanity and regression" 
4> Only sanity test which are not belongs to regression ----> pytest pytest_python\test_grouping.py -v -s -m "sanity" -m "not regression"
5> Only Regression which are not belongs to sanity -----> pytest pytest_python\test_grouping.py -v -s -m "regression " -m "not sanity"

'''