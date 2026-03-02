import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util

df = pd.read_csv("shl_assessments.csv")
df.columns = df.columns.str.strip()

model = SentenceTransformer("all-MiniLM-L6-v2")

# Precompute embeddings once
query_embeddings = model.encode(df["Query"].tolist(), convert_to_tensor=True)

def recommend_assessments(user_input):
    if not user_input.strip():
        return []

    user_embedding = model.encode(user_input, convert_to_tensor=True)

    similarities = util.cos_sim(user_embedding, query_embeddings)[0]

    top_k = torch.topk(similarities, k=3)

    results = []
    for score, idx in zip(top_k.values, top_k.indices):
        results.append(df.iloc[idx]["Assessment_url"])

    return results
