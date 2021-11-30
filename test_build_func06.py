try:
    import build_func06
except ImportError:
    assert False, "Not found"

# check the value of a variable
def test_main_1():
    a = build_func06.a
    assert a == 3.456, "Value Error 'a'"

# check the answer
def test_main_2():
    answer = build_func06.answer
    assert answer == 3.46, "Value Error  'answer'"