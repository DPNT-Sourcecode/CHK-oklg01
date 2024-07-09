from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_empty(self):
        assert checkout_solution.checkout() == -1

    def test_checkout_invalid_sku(self):
        assert checkout_solution.checkout("E") == -1

    def test_checkout_valid_sku(self):
        assert checkout_solution.checkout("A") == 50