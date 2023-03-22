from project import create_username, create_password, password_complexity

def main():
    test_username()
    test_password_length()
    test_password_complexity()

def test_username():
    assert create_username('a') ==  1
    assert create_username('0') ==  1
    assert create_username('') ==  1
    assert create_username('username') == 0

def test_password_length():
    assert create_password("a") == 1
    assert create_password("....") == 1
    assert create_password("passwo") == 1
    assert create_password("abcdef") == 1

def test_password_complexity():
    assert password_complexity("12345678") == 1
    assert password_complexity("abcdefghhtu") == 1
    assert password_complexity("222463") == 1
    assert password_complexity("a12345678") == 0

if __name__ == "__main__":
    main()