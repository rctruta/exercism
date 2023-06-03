def square_distance_to_origin(x, y):
    return x**2 + y**2


def score(x, y):
    """
    Function that returns the earned points in a single toss of a Darts game.
    If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points.
    """
    if square_distance_to_origin(x, y) > 10 * 10:
        return 0
    elif square_distance_to_origin(x, y) > 5 * 5:
        return 1
    elif square_distance_to_origin(x, y) > 1:
        return 5
    else:
        return 10
