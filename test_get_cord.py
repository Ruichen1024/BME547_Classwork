import pytest

@pytest.mark.parametrize("tuple1,tuple2,x,expected", [((2,2),(5,5),7,7)])

def test_get_y(tuple1,tuple2,x,expected):
    from get_cord import get_y
    answer = get_y(tuple1,tuple2,x)
    assert answer == expected
