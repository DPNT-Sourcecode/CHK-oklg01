
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

    if skus not in SKUS:
        return -1

    return SKUS[skus]

