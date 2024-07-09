
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

SKUS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return -1

    # if "," in skus:
    #     sku_list = [s.strip() for s in skus.split(",")]

    total_price = 0
    for sku in skus:
        if sku not in SKUS:
            return -1

        total_price += SKUS[sku]

    return total_price

