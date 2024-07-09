from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_empty(self):
        assert checkout_solution.checkout("") == -1

    def test_checkout_invalid_sku(self):
        assert checkout_solution.checkout("E") == -1

    def test_checkout_valid_sku(self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_sku_list_cs(self):
        assert checkout_solution.checkout("A,B,C") == 100

    def test_checkout_invalid_sku_list_cs(self):
        assert checkout_solution.checkout("A,B,E") == -1

    def test_checkout_sku_list_whitespace_cs(self):
        assert checkout_solution.checkout("A, B,  C") == 100

    def test_checkout_sku_list(self):
        assert checkout_solution.checkout("ABC") == 100

    def test_checkout_sku_invalid_list(self):
        assert checkout_solution.checkout("ABE") == -1

    def test_checkout_sku_whitespace(self):
        assert checkout_solution.checkout("AB   C") == 100
