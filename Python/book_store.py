from itertools import combinations

UNIT_PRICE = 800
PRICES = {k: UNIT_PRICE * k * (1 - v) for k, v in enumerate([0, .05, .1, .2, .25], 1)}
print(PRICES)

def total(books, shopping_price=0):
    """
    Compute the total cost of the books in the basket, such that the highest discount
    is obtained.
    """
    if len(books) == 0:
        return shopping_price

    books_distinct = set(books)
    books_groups = [books_distinct] + list(combinations(books_distinct, 4))
    
    best_price = None
    for books_to_sell in books_groups:
        books_remaining = books[:]
        for book in books_to_sell:
            books_remaining.remove(book)
        current_price = total(books_remaining, shopping_price + PRICES[len(books_to_sell)])
        best_price = current_price if best_price is None else min(best_price, current_price)
    
    return best_price
              
