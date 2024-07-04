import pytest
from stuff.accum import Accumulator

'''
Fixtures are special functions that pytest can call before test case functions. 
They're the best way to handle "Arrange" steps shared by multiple tests in the context 
of the Arrange-Act-Assert pattern.
'''


@pytest.fixture
def accum():
    return Accumulator()


@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    accum.add()  # act
    assert accum.count == 1  # assert


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accum.count = 10
