from ai.src.search import search

results = search("winter hiking jacket")

for r in results:
    print("Score:", r.score)
    print(r.payload["text"][:300])
    print("----")
