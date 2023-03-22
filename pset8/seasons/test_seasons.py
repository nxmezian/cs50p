from seasons import get_time

def main():
    test_input()

def test_input():
    assert get_time("2021-11-22") == 0


if __name__ == "__main__":
    main()