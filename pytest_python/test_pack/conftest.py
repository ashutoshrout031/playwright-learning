# conftest.py iis general fixture module accessible by other modules where all fixure functions are defined

import pytest

@pytest.fixture()
def setup():
    print("Setup environment")