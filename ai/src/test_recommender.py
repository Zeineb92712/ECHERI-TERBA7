from ai.src.recommender import recommend

results = recommend("warm lightweight mountain jacket")

for r in results:
    print("Score:", r.score)
    print(r.payload["text"][:300])
    print("----")
