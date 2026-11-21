import streamlit as st
import pandas as pd
import datetime as dt


#displays title and description
st.title("My Progress")
st.write("Check your streaks, completion rates, and activity chart.")

#checks if habits dataframe is available or not. if not then throw exception
try:
    habits_df = pd.read_csv("dataset/habit_tracker.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    habits_df = pd.DataFrame()

#checks if habit logs dataframe is available, if not then throw exception with columns Habit_Name and Completed_Date
try:
    logs_df = pd.read_csv("dataset/habit_logs.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    logs_df = pd.DataFrame(columns=["Habit_Name", "Completed_Date"])

#checks if habits dataframe is empty, if empty display info.
if habits_df.empty:
    st.info("No habits found yet. Go to 'Add Habit' to create one!")
else:
    today = dt.date.today() #store today's date in variable.

    # converts date type from csv to pandas date format
    if not logs_df.empty:
        logs_df["Completed_Date"] = pd.to_datetime(logs_df["Completed_Date"]).dt.date

    # create a loop to calculate and display metrics for each habit.
    for index, row in habits_df.iterrows():
        habit_name = row["Habit_Name"]
        start_date = pd.to_datetime(row["Start_Date"]).date()

        # filters logs to get dates where this habit was completed.
        habit_logs = logs_df[logs_df["Habit_Name"] == habit_name]
        logged_dates = sorted(habit_logs["Completed_Date"].unique(), reverse=True)

        # Completion Rate = (Days Completed / Total Days Since Start) * 100
        #calculates total days passed since start date.
        days_since_start = max((today - start_date).days + 1, 1)
        #calculates the percentage of active days completed. max 100%
        completion_rate = min(round((len(logged_dates) / days_since_start) * 100), 100)

        # count consecutive days logged backwards to find the streak.
        streak = 0
        check_date = today
        while check_date in logged_dates:
            streak += 1
            check_date -= dt.timedelta(days=1)

        # display the habit name and progress.
        st.subheader(habit_name)
        col1, col2 = st.columns(2)
        col1.metric("Current Streak", f"{streak} days")
        col2.metric("Completion Rate", f"{completion_rate}%")
        st.progress(completion_rate / 100)
        st.divider()

    # display the habit activity bar chart
    st.subheader("Total Completions per Habit")
    if logs_df.empty:
        st.write("Complete a habit in 'Log Habit' to see your chart!")
    else:
        counts = logs_df["Habit_Name"].value_counts()
        st.bar_chart(counts)
