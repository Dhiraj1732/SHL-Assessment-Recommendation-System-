import pandas as pd

df = pd.read_csv("shl_assessments.csv")

def recommend_assessments(query):
    query = query.lower()

    results = df[
        df["name"].str.lower().str.contains(query, na=False) |
        df["test_type"].str.lower().str.contains(query, na=False)
    ]

    return results.head(5)
