import pytest


# This file is for setup environment
# it's like base class in java selenium framework
# file name needs to be 'conftest.py'
# it's for generalize fixture and make it available to all test cases

# fixtures, similar to before and after test annotations
@pytest.fixture(scope="class")
def setup():
    print("I'll be executed first")
    yield
    print("I will be executed last")


# this is for DDT (check demo5)
@pytest.fixture()
def data_load():
    print('User profile data is being created')
    return ['John', 'Doe', 'amazon.com']


# Parameterize test with multiple data sets, this is example for cross-browser testing
# to send multiple datas with tuple or list
# DDT and parametrization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
@pytest.fixture(params=[("chrome", "two data together"), "firefox", "safari"])
def crossBrowser(request):
    return request.param


