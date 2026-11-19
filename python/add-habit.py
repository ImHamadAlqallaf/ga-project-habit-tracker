import streamlit as st

st.title("Add Habit")
st.write("Add new habits and keep track of your progress!")

habit_name = st.text_input("Habit Name", placeholder="Enter the habit name")
st.write("Habit name input is: " + habit_name)


frequency_int = st.number_input("Frequency", placeholder="Enter frequency number")
st.write("Frequency number is: "+ str(frequency_int))

