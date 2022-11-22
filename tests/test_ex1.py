"""
@pytest.mark.skip # skip test


@pytest.mark.xfail # used when we know that's going to fail

@pytest.mark.slow # custom marker
pytest -m "slow"

"""
import pytest


@pytest.fixture(scope='session')
def fixture_1():
    print('run-fixture-1')
    return 1


def test_exemple1(fixture_1):
    print('run-exemplo-1')
    num = fixture_1
    assert num == 1


# def test_exemple():
#     assert 1 == 1
#
#
# @pytest.mark.slow
# def test_exemple2():
#     assert 1 == 1
