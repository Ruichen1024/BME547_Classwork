import pytest

@pytest.mark.parametrize("tuple1,tuple2,x,expected", [((2,2),(5,5),7,7)])

def test_get_y(tuple1,tuple2,x,expected):
    from get_cord import get_y
    answer = get_y(tuple1,tuple2,x)
    assert answer == expected

@pytest.mark.parametrize("c1,c2,expected", [((1,2),(3,6),2)])

def test_get_slope(c1,c2,expected):
    from get_cord import get_slope
    answer = get_slope(c1,c2)
    assert answer == expected
