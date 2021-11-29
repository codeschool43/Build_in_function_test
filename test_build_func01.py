try:
    import build_func01
except ImportError:
    assert False, "Not found"

# checking answer value test#1
def test_main_1():
    number = build_func01.number
    assert number == -8, "Value Error 'number'"

# checking answer value test#2
def test_main_2():
    answer = build_func01.answer
    assert answer == 8, "Value Error  'answer'"