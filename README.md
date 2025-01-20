# personalised_recommendations_app
# Student Performance Analysis and Recommendations

This project is designed to analyze student performance data from quizzes, generate recommendations for improvement, and define student personas using clustering. It also includes visualizations to better understand performance trends.

## Features

1. **Data Fetching**:
   - Fetches historical and current quiz data from APIs.
   - Handles SSL certificate warnings for secure connections.

2. **Data Cleaning**:
   - Removes null values.
   - Processes nested columns like `quiz` to extract topics.
   - Converts and standardizes columns like `accuracy`.

3. **Performance Analysis**:
   - Analyzes student performance by topic.
   - Identifies weak areas (topics with low accuracy).

4. **Recommendations**:
   - Generates personalized recommendations for students based on their weak topics and difficulty levels.

5. **Student Persona Definition**:
   - Uses clustering to categorize students into personas (`Beginner`, `Intermediate`, `Advanced`) based on their performance data.

6. **Visualizations**:
   - Bar chart visualization of topic-wise accuracy using Matplotlib and Seaborn.

## Requirements

- Python 3.7+
- Libraries:
  - `requests`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `urllib3`

Install the required libraries using:
```bash
pip install -r requirements.txt
