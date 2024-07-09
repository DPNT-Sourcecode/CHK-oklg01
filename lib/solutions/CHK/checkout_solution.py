from collections import Counter

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+

SKUS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

SPECIALS = {
    "A": [{"num": 3, "discount": 20}, {"num": 5, "discount": 50}],
    "B": {"num": 2, "discount": 15},
    "E": {"num": 2, "discount": 30, "condition": "B"}
}

SPECIALS = [
    {"product": "A", "num": 5, "discount": 50},
    {"product": "A", "num": 3, "discount": 20},
    {"product": "E", "num": 2, "discount": 30, "condition": "B"},
    {"product": "B", "num": 2, "discount": 15},
    {"product": "F", "num": 3, "discount": 10, "condition": "F"},
    {"product": "H", "num": 10, "discount": 20},
    {"product": "H", "num": 5, "discount": 5},
    {"product": "K", "num": 2, "discount": 10},
    {"product": "N", "num": 3, "discount": 15, "condition": "M"},
    {"product": "P", "num": 5, "discount": 50},
    {"product": "R", "num": 3, "discount": 30, "condition": "Q"},
    {"product": "Q", "num": 3, "discount": 10},
    {"product": "U", "num": 3, "discount": 40, "condition": "U"},
    {"product": "V", "num": 3, "discount": 20},
    {"product": "V", "num": 2, "discount": 10},
]

def apply_specials_discount(item_counts):
    discount_total = 0
    for details in SPECIALS:
        product = details["product"]
        quantity = details["num"]
        discount = details["discount"]
        condition = details.get("condition")

        if condition:
            if not item_counts.get(condition) or not item_counts.get(condition) > 0:
                continue

        if product in item_counts:
            item_count = item_counts[product]
            if item_count >= quantity:
                discount_multiple = item_count // quantity
                discount_total += discount_multiple * discount
                items_used = quantity * discount_multiple
                item_counts[product] -= items_used
                if condition:
                    item_counts[condition] -= 1
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

