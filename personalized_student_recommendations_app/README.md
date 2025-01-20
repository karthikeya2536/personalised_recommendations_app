
# Personalized Student Recommendations - Flask App

This Flask application analyzes quiz performance and provides personalized recommendations for students to improve their preparation.

## Features
- Analyze current and historical quiz data.
- Generate insights on weak and strong topics.
- Provide actionable recommendations for improvement.

## Setup Instructions

1. Clone the repository or download the ZIP file.
2. Navigate to the project directory.
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```
   python app.py
   ```
5. Test the API using Postman or curl:
   - Endpoint: `http://127.0.0.1:5000/analyze`
   - Method: `POST`
   - Body: JSON (refer to `sample_request.json` for an example).

## Example Request
```json
{
    "current_quiz_data": [
        {"question_id": 1, "topic": "Physics", "difficulty": "medium", "correct": true},
        {"question_id": 2, "topic": "Chemistry", "difficulty": "hard", "correct": false},
        {"question_id": 3, "topic": "Biology", "difficulty": "easy", "correct": true}
    ],
    "historical_quiz_data": [
        {"quiz_id": 1, "topic": "Physics", "correct_responses": 8, "total_questions": 10},
        {"quiz_id": 1, "topic": "Chemistry", "correct_responses": 4, "total_questions": 10},
        {"quiz_id": 1, "topic": "Biology", "correct_responses": 9, "total_questions": 10}
    ]
}
```

## Example Response
```json
{
    "status": "success",
    "insights": {
        "weak_topics": ["Physics", "Chemistry"],
        "strength_topics": ["Biology"],
        "recommendations": [
            "Focus on solving medium and hard difficulty Physics questions.",
            "Revise key concepts in Chemistry."
        ]
    }
}
```
