from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_invalid_sku(self):
        assert checkout_solution.checkout("Z") == -1

    def test_checkout_valid_sku(self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_sku_list(self):
        assert checkout_solution.checkout("ABC") == 100

    def test_checkout_sku_invalid_list(self):
        assert checkout_solution.checkout("ABZ") == -1

    def test_checkout_sku_whitespace(self):
        assert checkout_solution.checkout("AB   C") == -1

    def test_checkout_special_offer(self):
        assert checkout_solution.checkout("ABABAD") == 190

    def test_checkout_multiple_special_offers(self):
        assert checkout_solution.checkout("AABAABABAAD") == 390

    def test_checkout_dup_special_same_item(self):
        assert checkout_solution.checkout("AAAAA") == 200