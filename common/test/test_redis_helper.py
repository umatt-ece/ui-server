from common import ParameterStore


def test_bool_value():
    # arrange
    ps = ParameterStore()
    # act
    value = ps.get(...)
    # assert
    assert value == False