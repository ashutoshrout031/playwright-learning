'''
Pre - Requisite : Install pytest-order plugin (previously pytest-ordering) 

pip install pytest-order 

'''

import pytest

# approach 1: order tests by position


# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")


# @pytest.mark.order(3)
# def test_addItem():
#     print("this is add item test")
# @pytest.mark.order(2)
# def test_logout():
#     print("this is logout")



# Approach:2
# Using before, after


# @pytest.mark.order()
# def test_addItem(before="test_checkout"):
#     print("this is add item test")
# @pytest.mark.order(after="test_addItem")
# def test_checkout():
#     print("this is checkout")

# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")

# Approach: 3 Using marker String (first and last)

@pytest.mark.order()
def test_addItem():
    print("this is add item test")
@pytest.mark.order("last")
def test_checkout():
    print("this is checkout")

@pytest.mark.order("first")
def test_login():
    print("this is login test")