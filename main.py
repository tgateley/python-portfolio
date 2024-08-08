import streamlit as st

st.set_page_config(layout="wide")

col1, cal2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with cal2:
    st.title("Tiffany Gateley")
    content = """ Hi, I am Tiffany! I am currently learning python on Udemy. I graduated in 2017
    from Arkansas Tech University with a B.S. in Mathematics. I enjoy learning new things and challenging my
    brain with puzzles.
    """
    st.write(content)
