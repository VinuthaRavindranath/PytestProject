import pytest


@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


'''
In Python, with is a special statement for automatically handling extra "enter" and "exit" logic
for a caller. It is most commonly used for file input and output. 
However, f or pytest.raises, the "enter" logic makes the code catch any exceptions, 
and the "exit" logic asserts if the desired exception type was actually raised.

'''


@pytest.mark.math
def test_divide_by_zero():
    # pytest.raises
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


print("------------------------------------To parametrize tests-------------------------------------------------")
products = [
    (2, 3, 6),  # positive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75)  # floats
]


@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


print("-------------------------------------------------------------------------------------")
