import streamlit as st
st.set_page_config(page_title="Chemistry Explorer", page_icon="🧪")
st.title("🧪 Chemistry Explorer") st.write("Welcome to your Cheminformatics App!")
compound = st.text_input("Enter a compound name", placeholder="Example: Aspirin")
if st.button("Search Compound"): if compound: st.info(f"You searched for: {compound}") st.write("Compound search feature is coming soon!") else: st.warning("Please enter a compound name.")
st.write("---") st.write("Created by a Chemistry Student 💗")
