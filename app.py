import streamlit as st
from recommender import recommend_assessments

st.set_page_config(page_title="SHL Assessment Recommender")

st.title("🧪 SHL Assessment Recommendation Engine")

query = st.text_area("Enter job description or query")

if st.button("Get Recommendations"):

    if not query.strip():
        st.warning("Please enter a query.")
    else:
        results = recommend_assessments(query)

        if results.empty:
            st.warning("No matching assessments found.")
        else:
            st.subheader("Recommended Assessments")
            for _, row in results.iterrows():
                st.markdown(f"### [{row['name']}]({row['url']})")
                st.write(f"Test Type: {row['test_type']}")
                st.write(f"Duration: {row['duration']}")
                st.write("---")
