import pandas as pd

df = pd.read_csv("shl_assessments.csv")

def recommend_assessments(user_input):
    user_input = user_input.lower().split()
    scored_results = []

    for _, row in df.iterrows():
        query_text = str(row["Query"]).lower()
        score = 0

        for word in user_input:
            if word in query_text:
                score += 1

        if score > 0:
            scored_results.append((score, row["Assessment_url"]))

    # Sort by score descending
    scored_results.sort(reverse=True)

    # Return top 3
    return [url for _, url in scored_results[:3]]
