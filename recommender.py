import pandas as pd

df = pd.read_csv("shl_assessments.csv")

# Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip()

def recommend_assessments(user_input):
    if "Query" not in df.columns or "Assessment_url" not in df.columns:
        return []

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

    scored_results.sort(reverse=True)

    return [url for _, url in scored_results[:3]]
