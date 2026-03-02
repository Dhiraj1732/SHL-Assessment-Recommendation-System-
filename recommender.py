import pandas as pd

# Load dataset
df = pd.read_csv("shl_assessments.csv")

# Clean column names
df.columns = df.columns.str.strip()

def recommend_assessments(query):
    if not query or not query.strip():
        return pd.DataFrame()

    query = query.lower()

    # Search inside name column
    filtered = df[df["name"].str.lower().str.contains(query, na=False)]

    return filtered.head(5)
