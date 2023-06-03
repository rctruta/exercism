def latest(scores):
    return scores[len(scores)-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return [score for score in sorted(scores)[::-1]][:3]
