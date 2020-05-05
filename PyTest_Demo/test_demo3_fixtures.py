import pytest


# fixtures, similar to before and after test annotations
@pytest.fixture()
def setup():
    print("I'll be executed first")
    yield
    print("I will be executed last")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")

