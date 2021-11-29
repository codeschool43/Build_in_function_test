try:
    import build_func04
except ImportError:
    assert False, "Not found"

# checking answer value test#1
def test_main_1():
    n = build_func04.n
    assert n ==4, "Value Error 'number'"

# checking answer value test#2
def test_main_2():
    answer = build_func04.answer
    assert answer == 4.0 , "Value Error  'answer'"