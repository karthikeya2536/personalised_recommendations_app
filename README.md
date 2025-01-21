# Personalized Student Recommendations App

This repository contains a Python-based application designed to generate personalized recommendations and analyze student performance based on historical quiz data. The app leverages machine learning techniques, such as clustering, to categorize students and provide tailored suggestions.

## Features

- **Data Collection**: Fetches historical and current quiz data from external APIs.
- **Data Cleaning**: Handles missing values and processes data (e.g., accuracy, topic, difficulty).
- **Performance Analysis**: Analyzes student performance across various quiz topics.
- **Recommendations**: Generates recommendations based on weak areas identified in a student's performance.
- **Persona Definition**: Uses KMeans clustering to categorize students into different personas (e.g., Beginner, Intermediate, Advanced).
- **Visualization**: Provides visualizations of student performance, including accuracy across topics.

## Installation

### Prerequisites

To run the project, you need the following:

- Python 3.6 or higher
- Required Python libraries (listed in `requirements.txt`)

### Setup

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/karthikeya2536/personalised_recommendations_app.git
    cd personalised_recommendations_app
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Data Sources

- **Historical Data**: Data is fetched from `https://api.jsonserve.com/XgAgFJ`.
- **Current Data**: Data is fetched from `https://jsonkeeper.com/b/LLQT`.

## Usage

1. After setting up, you can run the main script:

    ```bash
    python app.py
    ```

2. The script will:
   - Fetch the data from the APIs.
   - Clean and process the data.
   - Perform performance analysis and generate recommendations for a given student.
   - Define student personas using clustering (KMeans).
   - Display visualizations of student performance.

3. Modify the `student_id` in the main script to analyze a different student.

## Results

The script generates:
- **Recommendations** for improvement based on the student's weak topics.
- **Student Personas** categorized into Beginner, Intermediate, and Advanced groups.
- **Performance Visualizations** showing the accuracy for each topic.





