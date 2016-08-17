from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('tutorial.feature', 'run a simple test')
def test_run_a_simple_test():
    """run a simple test."""

@scenario('tutorial.feature', 'rerun a simple test')
def test_rerun_a_simple_test():
    """rerun a simple test."""



