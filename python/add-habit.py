import streamlit as st
import pandas as pd
import datetime as dt

#Displays the page title and description
st.title("Add Habit")
st.write("Add new habits and keep track of your progress!")

#stores user's input of habit name into a variable
habit_name = st.text_input("Habit Name", placeholder="Enter the habit name")
st.write("Habit name input is: " + habit_name)

#stores how many times the user does this habit in a day.
frequency_int = st.number_input("Frequency", placeholder="Enter frequency number", step = 1)
st.write("Frequency number is: "+ str(frequency_int))

#stores what the user's target goal is in a variable
target_goal = st.text_input("Target Goal", placeholder="Enter target goal")
st.write("Your target goal is: "+ target_goal)

#stores the habit category input by a user.
habit_category = st.text_input("Category", placeholder="Enter Category")
st.write("Your category is: "+ habit_category)

#lets the user input the date starting from (either today or >).
habit_start_date = st.date_input("Start Date", format="DD/MM/YYYY", min_value = dt.date.today())
st.write("Your start date is: "+ str(habit_start_date))

#lists the summary of the user's input in a list to confirm before pressing done.
st.markdown(f'''
To summarize:
- Your new habit name is {habit_name}
- Your frequency is {frequency_int}
- Your category is {habit_category}
- Your target goal is {target_goal}
- And you will start {str(habit_start_date)}
''')

#creates a button and checks in an if statement if pressed.
if st.button("Add Habit"):
    if habit_name and frequency_int and target_goal and habit_category and habit_start_date: #checks if these input fields are filled.

        #store them in a dataframe
        new_row = pd.DataFrame({
            "Habit_Name" : [habit_name],
            "Frequency" : [frequency_int],
            "Target_Goal" : [target_goal],
            "Category" : [habit_category],
            "Start_Date" : [habit_start_date]
        })

        new_row
        #check if habit_tracker file is available, else throw an exception
        #if available: concatenate new_row with the original dataset file
        #if not: store the new_row in new_df and create a new dataframe csv file.
        try: 
            original_df = pd.read_csv("dataset/habit_tracker.csv")
            new_df = pd.concat([original_df, new_row], ignore_index = True)
            #new_df = new_row.to_csv("dataset/habit_tracker.csv", index = False)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            new_df = new_row

        new_df.to_csv("dataset/habit_tracker.csv", index = False)
        st.success("Habit added successfully!")
        st.dataframe(new_df)

    else: #warning the user to fill in the right values.
        st.warning("Please fill in the missing values or correct themes") 
