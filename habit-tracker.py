import streamlit as st
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

try:
    st.logo("assets/habit-tracker-logo-2.png",size="large")
except FileNotFoundError:
    print("Logo file not found.")
    


pages = {
    "Habits": [
        st.Page("python/add-habit.py", title="Add Habit"),
        st.Page("python/log-habit.py", title="Log Habit"),
        st.Page("python/manage-habits.py", title="Manage Habits"),
    ],
    "Progress": [
        st.Page("python/my-progress.py", title="Habit Progress")
    ]
}

pg = st.navigation(pages)
pg.run()

