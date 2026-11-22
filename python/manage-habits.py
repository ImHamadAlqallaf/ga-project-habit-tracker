import streamlit as st
import pandas as pd

#display title and description
st.title("Manage Habits")
st.write("Edit or delete your habits below, or upload/download your CSV.")

#check if habits tracker is available, throw exception if not available.
#if not available, store columns in dataframe variable.
try:
    habits_df = pd.read_csv("dataset/habit_tracker.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    habits_df = pd.DataFrame(columns=["Habit_Name", "Frequency", "Target_Goal", "Category", "Start_Date"])

# able to interact with table by editing a cell or deleting rows.
#num_rows being dynamic allows the user to edit the rows and cells.
edited_df = st.data_editor(habits_df, num_rows="dynamic", width="content")

# creates 2 columns for Save Changes and Download CSV button equal column size
col1, col2 = st.columns(2)

#this button overwrites any changes made in the interactive table into the old habit_tracker file
with col1:
    if st.button("Save Changes", type="primary"):
        edited_df.to_csv("dataset/habit_tracker.csv", index=False)
        st.success("Changes saved!")
        st.rerun()

#converts current dataframe into utf-8 csv so browser is able to download
with col2:
    csv_data = edited_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="habit_tracker.csv",
        mime="text/csv"
    )

st.divider() #creates a divider 

#upload button to upload csv files with type "csv" only.
uploaded_file = st.file_uploader("Upload a Habits CSV", type="csv")
#checks if uploaded_file does not contain empty values 
if uploaded_file is not None:
    if st.button("Import CSV"): #creates import button and loads new dataset and overwrites old dataset.
        try:
            new_df = pd.read_csv(uploaded_file)
            new_df.to_csv("dataset/habit_tracker.csv", index=False)
            st.success("CSV imported!")
            st.rerun()
        except pd.errors.EmptyDataError:
            st.error("The uploaded CSV file is empty!")
