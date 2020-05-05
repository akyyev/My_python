import pytest


def test_program(setup):
    msg = 'Hello'
    assert msg == 'Hello'
    assert len(msg) == 5
    print('Everything went well')


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_demo1(self):
        print('Demo 1')

    def test_demo2(self):
        print('Demo 2')

    def test_demo3(self):
        print('Demo 3')

    def test_demo4(self):
        print('Demo 4')
