from ai.src.search import search

def recommend(user_need: str, limit=5):
    return search(user_need, limit)
