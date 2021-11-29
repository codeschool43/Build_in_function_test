try:
    import build_func04
except ImportError:
    assert False, "Not found"

# checking value n
def test_main_1():
    n = build_func04.n
    assert n == 3, "Value Error 'n'"

# checking value x
def test_main_2():
    x = build_func04.x
    assert x == 6, "Value Error  'x'"

def test_main_2():
    answer = build_func04.answer
    assert answer == 945, "Value Error  'answer'"