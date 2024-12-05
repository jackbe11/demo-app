import streamlit as st

#st.write("My first streamlit app")
title = st.text_input("Please input string to be reversed: ")
st.write("The reversed string is: ", title[::-1])
