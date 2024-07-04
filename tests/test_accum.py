import pytest
from stuff.accum import Accumulator


@pytest.mark.accumulator
def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0


'''
This pattern is called "Arrange-Act-Assert". It is the classic three-step pattern for functional test cases.
1. Arrange assets for the test (like a setup procedure).
2. Act by exercising the target behavior.
3. Assert that expected outcomes happen.
Independent, atomic tests make failure analysis easier in the event of a regression.
'''


@pytest.mark.accumulator
def test_accumulator_add_one():
    accum = Accumulator()  # arrange
    accum.add()  # act
    assert accum.count == 1  # assert


@pytest.mark.accumulator
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accum.count = 10
