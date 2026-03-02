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
