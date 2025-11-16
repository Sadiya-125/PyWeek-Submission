import streamlit as st
import pandas as pd
import numpy as np
import time

# --- TEXT DISPLAY ---
st.title("STREAMLIT (PYWEEK)")
st.header("Welcome to Streamlit Demo")
st.subheader("Interactive Widgets Example")
st.text("My name is Sadiya Maheen Siddiqui.")
st.markdown("**UCEOU**")
st.caption("My details")
st.code("print('Hello Streamlit!')")
st.latex(r"E = mc^2")

# --- INPUT WIDGETS ---
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 0, 100)
gender = st.radio("Select gender", ["Male", "Female"])
hobbies = st.multiselect("Select hobbies", ["Reading", "Gaming", "Traveling", "Coding","Sports"])
rating = st.slider("Rate PYWEEK", 1, 10, 5)
date = st.date_input("Pick a date")
color = st.color_picker("Pick a color")

if st.button("Submit"):
    st.write(f"Name: {name}, Age: {age}, Gender: {gender}, Rating: {rating}")
    st.write("Hobbies:", hobbies)
    st.write("Favorite color:", color)
    st.success("Form Submitted!")

# --- DISPLAY DATA ---
data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.write(data)
st.dataframe(data)
st.table(data)

# --- CHARTS ---
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

# --- SIDEBAR ---
st.sidebar.title("Sidebar Example")
choice = st.sidebar.selectbox("Choose an option", ["Home", "Data", "About"])
st.sidebar.write("You selected:", choice)

# --- LAYOUT WITH COLUMNS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
    st.camera_input("Take a picture here")

with col2:
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with col3:
    st.audio_input("Record your audio")

# --- EXPANDER ---
with st.expander("Expand for more"):
    st.write("This content is hidden inside an expander.")

# --- CONDITIONAL CAMERA ---
enable = st.checkbox("Enable extra camera")
picture = st.camera_input("Optional camera", disabled=not enable)

if picture:
    st.image(picture)

# --- CACHED FUNCTION EXAMPLE ---
@st.cache_data
def get_data():
    time.sleep(2)
    return pd.DataFrame(np.random.randn(5, 2), columns=["X", "Y"])

if st.button("Load Cached Data"):
    df = get_data()
    st.dataframe(df)

# --- STATUS MESSAGES ---
st.success("Operation Successful!")
st.warning("This is a warning!")
st.error("This is an error message!")
st.info("This is an info message!")

# --- PROGRESS BAR ---
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)
st.balloons()
