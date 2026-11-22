# Habit Tracker Web App

A simple, interactive web application built with **Streamlit** and **Pandas** to help users build daily habits, track streaks, and visualize progress over time.

## Live Demo & Links

* **Deployed App:** [Habit Tracker Live App](https://hamados-ga-habit-tracker.streamlit.app/)
* **Video Demonstration:** [Watch Video Walkthrough](PASTE_YOUR_VIDEO_LINK_HERE)

## Features

* **Add Habit:** Create new habits with a custom name, daily frequency, target goal, category, and start date.
* **Log Habit:** Check off daily habits with one click, prevent duplicate check-ins on the same day, and celebrate 7-day streaks with balloons.
* **My Progress:** View current streaks, completion rates, progress bars, and an activity bar chart comparing completions across habits.
* **Manage Habits:** Edit habit details directly in an interactive table, delete unwanted rows, and import/export habit data as CSV files.

## Project Structure

```text
habit-tracker/
├── habit-tracker.py        # Main entry point and sidebar navigation
├── assets/
│   └── habit-tracker-logo-2.png
├── dataset/
│   ├── habit_tracker.csv   # Stores active habits
│   └── habit_logs.csv      # Stores daily completion history
└── python/
    ├── add-habit.py        # Create new habits
    ├── log-habit.py        # Daily check-ins and streak rewards
    ├── my-progress.py      # Streaks, completion rates, and charts
    └── manage-habits.py    # Edit, delete, upload, and download CSVs
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install streamlit pandas
   ```

2. **Run the application:**
   ```bash
   streamlit run habit-tracker.py
   ```
