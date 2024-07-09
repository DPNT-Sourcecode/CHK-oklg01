from solutions.HLO import hello_solution


class TestHello:
    def test_hello_name(self):
        assert hello_solution.hello("Alan") == "Hello, Alan!"

    def test_hello_no_name(self):
        assert hello_solution.hello("") == "Hello, World!"