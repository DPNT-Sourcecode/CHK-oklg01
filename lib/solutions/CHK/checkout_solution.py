from collections import Counter

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

SKUS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

SPECIALS = {
    "A": [{"num": 3, "discount": 20}, {"num": 5, "discount": 50}],
    "B": {"num": 2, "discount": 15},
    "E": {"num": 2, "discount": 30, "condition": "B"}
}

def apply_specials_discount(item_counts):
    discount_total = 0
    for special, details in SPECIALS.items():
        if special in item_counts:
            item_count = item_counts[special]
            if item_count >= details["num"]:
                discount_total += (item_count // details["num"]) * details["discount"]
    return discount_total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0

    total_price = 0
    for sku in skus:
        if sku not in SKUS:
            return -1

        total_price += SKUS[sku]

    discounts = apply_specials_discount(Counter(skus))

    return total_price - discounts

