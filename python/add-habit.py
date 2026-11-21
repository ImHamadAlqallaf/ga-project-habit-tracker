import streamlit as st
import pandas as pd
import datetime as dt

st.title("Add Habit")
st.write("Add new habits and keep track of your progress!")

habit_name = st.text_input("Habit Name", placeholder="Enter the habit name", required = True)
st.write("Habit name input is: " + habit_name)

frequency_int = st.number_input("Frequency", placeholder="Enter frequency number", required = True, step = 1)
st.write("Frequency number is: "+ str(frequency_int))

target_goal = st.text_input("Target Goal", placeholder="Enter target goal", required = True)
st.write("Your target goal is: "+ target_goal)

habit_category = st.text_input("Category", placeholder="Enter Category", required = True)
st.write("Your category is: "+ habit_category)

habit_start_date = st.date_input("Start Date", format="DD/MM/YYYY", required = True, min_value = "today")
st.write("Your start date is: "+ str(habit_start_date))

st.markdown(f'''
To summarize:
- Your new habit name is {habit_name}
- Your frequency is {frequency_int}
- Your category is {habit_category}
- Your target goal is {target_goal}
- And you will start {str(habit_start_date)}
''')

# st.button("Add Habit", type="secondary")
if st.button("Add Habit"):
    if habit_name and frequency_int and target_goal and habit_category and habit_start_date:
    
        new_row = pd.DataFrame({
            "Habit_Name" : [habit_name],
            "Frequency" : [frequency_int],
            "Target_Goal" : [target_goal],
            "Category" : [habit_category],
            "Start_Date" : [habit_start_date]
        })

        new_row
        try: 
            original_df = pd.read_csv("dataset/habit_tracker.csv")
            new_df = pd.concat([original_df, new_row], ignore_index = True)
            #new_df = new_row.to_csv("dataset/habit_tracker.csv", index = False)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            new_df = new_row

        new_df.to_csv("dataset/habit_tracker.csv", index = False)
        st.success("Habit added successfully!")
        st.dataframe(new_df)

    else:
        st.warning("Please fill in the missing values or correct themes")
        




