```python
def ai_agent():
    print("Welcome to Basic AI Agent")
    print("I am your personal study assistant.")

    problem = input("Enter your problem: ").lower()

    if "study" in problem:
        print("AI Suggestion: Make a study timetable and follow it daily.")

    elif "tired" in problem:
        print("AI Suggestion: Take some rest and refresh your mind.")

    elif "python" in problem:
        print("AI Suggestion: Practice Python programs regularly.")

    elif "exam" in problem:
        print("AI Suggestion: Revise important topics and solve previous questions.")

    elif "time" in problem:
        print("AI Suggestion: Prepare a daily schedule and prioritize your tasks.")

    elif "project" in problem:
        print("AI Suggestion: Divide your project into small tasks and complete them step by step.")

    else:
        print("AI Suggestion: Please explain your problem clearly.")

ai_agent()
```
