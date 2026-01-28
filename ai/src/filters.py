def filter_by_score(results, min_score=0.4):
    return [r for r in results if r.score >= min_score]
