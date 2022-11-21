"""
@pytest.mark.skip # skip test


@pytest.mark.xfail # used when we know that's going to fail

@pytest.mark.slow # custom marker
pytest -m "slow"

"""
import pytest


def test_exemple():
    assert 1 == 1

@pytest.mark.slow
def test_exemple2():
    assert 1 == 1
