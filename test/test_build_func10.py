try:
    import build_func08
except ImportError:
    assert False, "Not found"

# check the value of a variable
def test_main_1():
    x = build_func08.x
    assert x == 2, "Value Error 'x'"

# check the value of a variable
def test_main_2():
    y = build_func08.y
    assert y == 4, "Value Error  'y'"

# check the answer
def test_main_2():
    answer = build_func08.answer
    assert answer == 7.59, "Value Error  'answer'"