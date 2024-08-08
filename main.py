import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, cal2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)


with cal2:
    st.title("Tiffany Gateley")
    content = """ Hi, I am Tiffany! I am currently learning python on Udemy. I graduated in 2017
    from Arkansas Tech University with a B.S. in Mathematics. I enjoy learning new things and challenging my
    brain with puzzles.
    """
    st.write(content)

content2 = """Below you can find some of the apps
         I have built in Python, Feel fee to contact me! """
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row, in df[:10].iterrows():

        st.subheader((row["title"]))
        st.write(row["description"])
with col4:
    for index, row, in df[10:].iterrows():
        st.subheader((row["title"]))
        st.write(row["description"])