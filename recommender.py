import pandas as pd

df = pd.read_csv("shl_assessments.csv")

def recommend_assessments(user_input):
    if "Query" not in df.columns:
        return []

    user_input = user_input.lower()
    results = []

    for _, row in df.iterrows():
        query_text = str(row["Query"]).lower()

        if user_input in query_text:
            results.append(row["Assessment_url"])

    return results
