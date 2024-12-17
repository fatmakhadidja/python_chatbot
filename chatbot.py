import json
import os


# File path for saving responses
response_file = "responses.json"

# Function to load responses from a file, or use default if file doesn't exist
def load_responses():
    if os.path.exists(response_file):
        with open(response_file, "r") as file:
            return json.load(file)
    else:
        return default_responses

# Function to save responses to a file
def save_responses(responses):
    with open(response_file, "w") as file:
        json.dump(responses, file, indent=4)

def chatbot():
    # Load responses from file (or use defaults if the file doesn't exist)
    responses = load_responses()

    print("Hello, I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Take user input and convert it to lowercase
        
        # Check for responses
        if user_input in responses:
            print(f"Bot: {responses[user_input]}")
        else:
            print(f"Bot: {responses['default']}")
            # If the bot doesn't know the response, ask the user and store it
            new_response = input("I don't know that yet. Can you tell me what to say? ")
            responses[user_input] = new_response
            print(f"Bot: Thanks! I'll remember that next time.")
            save_responses(responses)  # Save the updated responses to the file

        if user_input == "bye":
            print("Bot: Goodbye!")
            break

chatbot()
