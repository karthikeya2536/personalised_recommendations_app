import requests
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import urllib3

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Fetch data from APIs
def fetch_data(url):
    try:
        response = requests.get(url, verify=False)  # Ignore SSL certificate verification
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Load historical and current quiz data
historical_data_url = "https://api.jsonserve.com/XgAgFJ"
current_data_url = "https://jsonkeeper.com/b/LLQT"

historical_data = fetch_data(historical_data_url)
current_data = fetch_data(current_data_url)

historical_df = pd.DataFrame(historical_data)
current_df = pd.DataFrame(current_data)

# Clean data
historical_df.dropna(inplace=True)
current_df.dropna(inplace=True)

# Add 'topic' column if 'quiz' is present
if 'quiz' in historical_df.columns:
    historical_df['topic'] = historical_df['quiz'].apply(
        lambda x: x['title'] if isinstance(x, dict) and 'title' in x else None
    )

# Clean 'accuracy' column (remove '%' and convert to float)
if 'accuracy' in historical_df.columns:
    historical_df['accuracy'] = historical_df['accuracy'].replace(r'\s*%', '', regex=True).astype(float)

# Handle missing 'difficulty' column
if 'difficulty' not in historical_df.columns:
    print("'difficulty' column not found. Adding default value.")
    historical_df['difficulty'] = "Unknown"

# 1. Performance Analysis
topic_accuracy = historical_df.groupby('topic')['correct_answers'].mean()

# Weak areas
weak_topics = topic_accuracy[topic_accuracy < 10]  # Adjust threshold as needed

# 2. Generate Recommendations
def generate_recommendations(student_id):
    # Filter user data based on student_id
    user_data = historical_df[historical_df['id'] == student_id]

    # Check if user_data is empty
    if user_data.empty:
        print(f"No data found for student_id: {student_id}")
        return ["No data available for this user."]

    # Calculate weak topics
    weak_topics_user = user_data.groupby('topic')['correct_answers'].mean()
    weak_topics_user = weak_topics_user[weak_topics_user < 10]  # Adjust threshold as needed

    recommendations = []
    
    # Check if there are any weak topics
    if not weak_topics_user.empty:
        recommendations.append(f"Focus on these weak topics: {', '.join(weak_topics_user.index)}")
    else:
        recommendations.append("All topics seem well-covered. Keep up the good work!")

    # Analyze difficulty if available
    if 'difficulty' in user_data.columns and not user_data['difficulty'].isnull().all():
        weak_difficulties_user = user_data.groupby('difficulty')['correct_answers'].mean()
        weak_difficulties_user = weak_difficulties_user[weak_difficulties_user < 10]  # Adjust threshold as needed

        # Check if there are any weak difficulties
        if not weak_difficulties_user.empty:
            recommendations.append(f"Practice easier questions at these difficulty levels: {', '.join(weak_difficulties_user.index)}")

    return recommendations

# 3. Persona Definition using Clustering
def define_student_persona():
    # Encode categorical features for clustering
    le_topic = LabelEncoder()
    le_difficulty = LabelEncoder()

    historical_df['encoded_topic'] = le_topic.fit_transform(historical_df['topic'])

    # Process difficulty if it exists
    if 'difficulty' in historical_df.columns:
        historical_df['encoded_difficulty'] = le_difficulty.fit_transform(historical_df['difficulty'])
    else:
        historical_df['encoded_difficulty'] = np.zeros(len(historical_df))

    # Standardize numerical features
    scaler = StandardScaler()
    historical_df['scaled_accuracy'] = scaler.fit_transform(historical_df[['accuracy']])

    # Check if clustering is feasible
    if len(historical_df) < 3:
        print("Not enough data for clustering.")
        return

    # Perform clustering
    features = historical_df[['scaled_accuracy', 'encoded_difficulty', 'encoded_topic']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    historical_df['persona'] = kmeans.fit_predict(features)

    persona_map = {0: "Beginner", 1: "Intermediate", 2: "Advanced"}
    historical_df['persona_label'] = historical_df['persona'].map(persona_map)

    # Create a structured output for student persona
    high_performers = historical_df[historical_df['persona'] == 2]['id'].tolist()
    needs_improvement = historical_df[historical_df['persona'] == 0]['id'].tolist()

    return {
        'high_performer': high_performers,
        'needs_improvement': needs_improvement
    }

# 4. Visualizations
def plot_performance():
    plt.figure(figsize=(10, 6))
    sns.barplot(x=topic_accuracy.index, y=topic_accuracy.values)
    plt.title("Accuracy by Topic")
    plt.xticks(rotation=90)
    plt.xlabel("Topic")
    plt.ylabel("Accuracy")
    plt.tight_layout()
    plt.show()

# Function to find a student ID with weak topics
def find_student_with_weak_topics():
    weak_students = historical_df[historical_df['topic'].isin(weak_topics.index)]
    return weak_students['id'].unique().tolist()

# Main execution
if __name__ == "__main__":
    # Use a valid student ID
    student_id = 321514

    # Generate recommendations
    recommendations = generate_recommendations(student_id)
    print("Recommendations:")
    for rec in recommendations:
        print(f"- {rec}")

    # Define student persona
    student_persona = define_student_persona()
    print("Student Persona:")
    print(student_persona)

    # Find students with weak topics
    students_with_weak_topics = find_student_with_weak_topics()
    print("Students with Weak Topics:")
    print(students_with_weak_topics)

    # Plot visualizations
    plot_performance()