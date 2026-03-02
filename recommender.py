import pandas as pd

def load_data():
    return pd.read_csv("shl_assessments.csv")

def recommend_assessments(user_input, top_n=3):
    df = load_data()
    
    user_input = user_input.lower()
    
    scores = []
    
    for _, row in df.iterrows():
        skills = row["Skills"].lower()
        match_score = sum(1 for word in user_input.split() if word in skills)
        scores.append(match_score)
    
    df["Match Score"] = scores
    df = df.sort_values(by="Match Score", ascending=False)
    
    return df.head(top_n)
