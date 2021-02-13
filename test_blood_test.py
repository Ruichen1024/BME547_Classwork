import pytest

@pytest.mark.parametrize("para,expected", [(65,"Normal"),(45,"Borderline low"),(20,"Low")])

# def test_analyze_HDLdata_1():
#     from blood_test import analyze_HDLdata
#     answer1 = analyze_HDLdata(65)
#     expected1 = "Normal"
#     assert answer1 == expected1
#
# def test_analyze_HDLdata_2():
#     from blood_test import analyze_HDLdata
#     answer2 = analyze_HDLdata(45)
#     expected2 = "Borderline low"
#     assert answer2 == expected2
#
# def test_analyze_HDLdata_3():
#     from blood_test import analyze_HDLdata
#     answer3 = analyze_HDLdata(20)
#     expected3 = "Low"
#     assert answer3 == expected3

def test_analyze_HDLdata(para,expected):
    from blood_test import analyze_HDLdata
    answer = analyze_HDLdata(para)
    assert answer == expected
