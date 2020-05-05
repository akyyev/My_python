# PyTest rules
# Any PyTest file should start with test_ or _test
# PyTest methods must start with test
# All codes should be wrapped with method
# To run from console just go to that directory and type:
#       py.test                         plain
#       py.test -v                      more detailed
#       py.test -v -s                   with console output
#       py.test -v -s -k credit_cart    to run only tests with name contains credit_cart
#  -k stands for method names execution, -s logs in output, -v stands for more info metadata

# we can run specific file with py.test <filename>
import pytest


@pytest.mark.xfail
# we mark it xfail if it's mandatory for other test cases
# but we don't want to include test result to report
def test_program():
    msg = 'Hello'
    assert msg == 'Hi'


@pytest.mark.smoke
def test_credit_cart_test():
    assert 40 - 30 == 10


