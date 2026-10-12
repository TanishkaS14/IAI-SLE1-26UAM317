def ai_agent():
    print("Welcome to Personal Health & Fitness AI Agent")
    print("I am your personal fitness assistant.")

    problem = input("\nEnter your problem (or type 'exit' to stop): ").lower()

        # Check if the user wants to quit the program
        if problem == "exit":
            print("Exiting AI Agent. Stay healthy!")
            break  # This breaks out of the loop and stops the program


    elif "water" in problem:
        print("AI Suggestion: Drink water regularly throughout the day.")

    elif "exercise" in problem:
        print("AI Suggestion: Try regular physical activity suitable for you.")

    elif "sleep" in problem:
        print("AI Suggestion: Maintain a regular sleep schedule.")

    elif "stress" in problem:
        print("AI Suggestion: Try relaxation exercises and take short breaks.")

    elif "food" in problem:
        print("AI Suggestion: Eat a balanced diet with fruits and vegetables.")

    elif "walking" in problem:
        print("AI Suggestion: Include regular walking in your daily routine.")

    else:
        print("AI Suggestion: Please describe your fitness concern clearly.")

ai_agent()

