import streamlit as st
import datetime as dt
import pandas as pd

#displays the title and description
st.title("Log Habit")
st.write("Log your habits daily here to keep track of your progress")

# this checks if a 7-day streak milestone was just hit before st.rerun()
if "celebrate_habit" in st.session_state:
    st.success(f"🔥 7-Day Streak! You've completed '{st.session_state['celebrate_habit']}' for 7 days in a row!")
    st.balloons()
    del st.session_state["celebrate_habit"]  # delete session_state so balloons don't replay on every refresh

#shows the text of current active habits
st.text("Current Active Habits:")

#stores the date of today and then cast string type for today.
today = dt.date.today()
today_str = str(today)


#checks if habits tracker csv is available and throws exception if not.
try:
    habits_df = pd.read_csv("dataset/habit_tracker.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    habits_df = pd.DataFrame()


#show text indicating no habits available.
if habits_df.empty:
    st.info("No habits available, add your habits now to view and log it here!")
else:

    #checks if habit_logs is available, if not then throw exception.
    try:
        logs_df = pd.read_csv("dataset/habit_logs.csv")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        logs_df = pd.DataFrame(columns=["Habit_Name", "Completed_Date"])


    #iterate through each row of habits data frame
    for index, row in habits_df.iterrows():
        habit_name = row["Habit_Name"]

        #this filters out if today's completed date does exist and stores in variable.
        already_logged = not logs_df[
            (logs_df["Habit_Name"] == habit_name) & 
            (logs_df["Completed_Date"] == today_str)
        ].empty

        #create 2 columns, one takes 75% (3) for the details and the other takes 25% (1) for completed button.
        column1, column2 = st.columns([3,1])

        #column 1 contains the details of the habit. iterating through the rows 
        with column1:
            st.subheader(habit_name)
            st.caption(f"Goal: {row['Target_Goal']} | Category: {row['Category']}")

        #column2 contains the complete button.
        with column2:
            #checks user is already logged, display "Done" and make the button unable to click. and button is given an index
            # - based on the habit
            if already_logged:
                st.button("Done!", key=f"btn_{index}", disabled=True)
            else:
                #creates a Complete Button with the row index, if clicked, add the habit_name and completed_date (today's date) to a variable and concatinate it with the original logs_df.
                if st.button("Complete", key=f"btn_{index}"):
                    new_log = pd.DataFrame({
                        "Habit_Name": [habit_name],
                        "Completed_Date": [today_str]
                    })
                    logs_df = pd.concat([logs_df, new_log], ignore_index=True)
                    logs_df.to_csv("dataset/habit_logs.csv", index=False)

                    # collects all unique completed date to calculate current streak
                    habit_dates = pd.to_datetime(
                        logs_df[logs_df["Habit_Name"] == habit_name]["Completed_Date"]
                    ).dt.date.unique()

                    #count consecutive days backwards starting from "today"
                    streak = 0
                    check_date = today
                    while check_date in habit_dates:
                        streak += 1
                        check_date -= dt.timedelta(days=1)

                    #store habit name in session_state so that balloons pop up right after st.rerun()
                    if streak == 7:
                        st.session_state["celebrate_habit"] = habit_name

                    st.rerun()

        st.divider() #adds a line in between each habit
