scores = []
def add_score(value):
    scores.append(value)
    return "Score added!"

def remove_score(value):
    if value in scores:
        scores.remove(value)
        return "Scores removed!"
    return "Scores not found."

def display_scores():
    if not scores:
        return "No scores yet."
    return f"Scores: {scores}"