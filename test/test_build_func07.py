try:
    import build_func07
except ImportError:
    assert False, "Not found"

# check the value of a variable
def test_main_1():
    x = build_func07.x
    assert x == 5, "Value Error 'x'"

# check the value of a variable
def test_main_2():
    y = build_func07.y
    assert y == 2, "Value Error  'y'"

# check the answer
def test_main_2():
    answer = build_func07.answer
    assert answer == 805, "Value Error  'answer'"