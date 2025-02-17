def hybrid_search(vector_results, keyword_results, weight=0.7):
    combined = {}

    # Normalize ranking scores
    for rank, (id, _) in enumerate(vector_results):
        combined[id] = combined.get(id, 0) + (1 - rank/10) * weight

    for rank, (id, _) in enumerate(keyword_results):
        combined[id] = combined.get(id, 0) + (1 - rank/10) * (1 - weight)

    return sorted(combined.items(), key=lambda x: -x[1])

# Example
vector_results = [(2, 0.1), (1, 0.2)]  # Banana, Apple
keyword_results = [(3, 0.9), (1, 0.8)]  # Carrot, Apple

print(hybrid_search(vector_results, keyword_results))
