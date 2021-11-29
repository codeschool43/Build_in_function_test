try:
    import build_func02
except ImportError:
    assert False, "Not found"

# checking answer value
def test_main_1():
    answer = build_func02.answer
    assert answer == 10.95, "Value Error 'answer'"