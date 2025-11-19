from score_utilis import scores

def average_scores():
    if len(scores) == 0:
        return "No scores to average."
    return sum(scores) / len(scores)
