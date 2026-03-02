import streamlit as st
from recommender import recommend_assessments

st.set_page_config(page_title="SHL Assessment Recommendation Engine")

st.title("SHL Assessment Recommendation Engine")

st.write("Enter job role or required skills to get recommended assessments.")

user_input = st.text_input("Enter Job Role or Skills")

if user_input:
    results = recommend_assessments(user_input)

    st.subheader("Top Recommended Assessments")
    st.dataframe(results)

    st.success("Recommendations generated successfully!")
