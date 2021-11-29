try:
    import build_func05
except ImportError:
    assert False, "Not found"

# checking value n
def test_main_1():
    n = build_func05.n
    assert n == 3, "Value Error 'n'"

# checking value x
def test_main_2():
    x = build_func05.x
    assert x == 6, "Value Error  'x'"

def test_main_2():
    answer = build_func05.answer
    assert answer == 945, "Value Error  'answer'"