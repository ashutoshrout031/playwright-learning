import pytest

# def test_one():
#     print("This is test one")

# def test_two():
#     print("This is test two")

# def test_three():
#     print("This is test three")
    
# def test_four():
#     assert 1+1 ==2


# pytest modulename.py -s to execute the print statements
# pytest modulename.py::functionname -s <-v> (more detailinfo) 
'''
To Run all the test in the module
    pytest test_demo.py
    pytest test_demo.py -s 
    pytest test_demo.py -s -v

To Run specific test in the module
    pytest test_demo.py::test_one -s -v
    pytest test_demo.py::test_two -s -v
    pytest test_demo.py::test_three -s -v

-s : You can see all print() outputs live in the console while the test runs
-v : Runs pytest in verbose mode. Shows detailed test execution information

'''

# test functuion inside the class

# class TestClass:
#     def test_one(self):
#         print("This is test one")

#     def test_two(self):
#         print("This is test two")

#     def test_three(self):
#         print("This is test three")
        
#     def test_four(self):
#         assert 1+1 ==2


def test_01():
    assert 1+1 == 3
    assert 2 <= 5
    assert 2*4 ==8

def test_02():
    assert 96<100
    # assert 1


def test_case_03():
    with pytest.raises(Exception):
        assert 3-1 == 1
