import streamlit as st
from recommender import recommend_assessments

st.set_page_config(page_title="SHL Assessment Recommendation Engine")

st.title("SHL Assessment Recommendation Engine")
st.write("Enter job role or required skills to get recommended assessments.")

user_input = st.text_input("Enter Job Role or Skills")

if user_input:
    results = recommend_assessments(user_input)

    if results:
        st.subheader("Top Recommended Assessments")
        for url in results:
            st.write(url)
    else:
        st.warning("No matching assessments found.")
        if st.button("Get Recommendations"):
    if user_input:
        results = recommend_assessments(user_input)

        if results:
            st.subheader("Top Recommended Assessments")
            for url in results:
                st.write(url)
        else:
            st.warning("No matching assessments found.")
    else:
        st.warning("Please enter job role or skills.")
