try:
    import build_func03
except ImportError:
    assert False, "Not found"

# checking answer value test#1
def test_main_1():
    n = build_func03.n
    assert n == 3.5, "Value Error 'number'"

# checking answer value test#2
def test_main_2():
    answer = build_func03.answer
    assert answer == 6.75 , "Value Error  'answer'"