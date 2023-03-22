def main():
    test_convert()
    test_gauge()

def test_convert():
    test_OSError()
    test_zero_division()

def test_OSError():
    with pytest.raises(OSError):
        convert("cat")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert(1/0)