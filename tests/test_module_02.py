class TestMyStuff():
    def test_add(self):
        assert 1 + 1 == 2

    def test_subtract(self):
        assert 5 - 3 == 2

    def test_string(self):
        assert str.upper('hello') == 'HELLO' # failing test, 'hello' should be converted to uppercase 'HELLO'
        assert 'world'.capitalize() == 'World'  # failing test, 'world' should be capitalized to 'World'