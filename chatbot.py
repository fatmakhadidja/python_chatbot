import json
from fuzzywuzzy import process
import random

jokes = [ 
    "Why did the developer go broke? Because he used up all his cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the developer go broke? Because he used up all his cache.",
    "What did the ocean say to the beach? Nothing, it just waved.",
    "Why don't skeletons fight each other? They don't have the guts!"
]

# File path for saving responses
response_file = "responses.json"

# Function to load responses from a file
def load_responses():
        with open(response_file, "r") as file:
            return json.load(file)
    

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
        
        # Find the best match to the user's input using fuzzywuzzy
        best_match = process.extractOne(user_input, responses.keys())  #best_match = [closest matching string,the similarity score (out of 100)]
       
        if best_match[1] >= 80:  # The threshold for similarity, adjust as needed
            if (responses[best_match[0]]=="RANDOM JOKE") :
                print(f"Bot: {random.choice(jokes)}")
            else :    
                 print(f"Bot: {responses[best_match[0]]}")
        else:
            print(f"Bot: {responses['default']}")
            # If the bot doesn't know the response, ask the user and store it
            new_response = input("I don't know that yet. Can you tell me what to say? -->  ")
            responses[user_input] = new_response
            print(f"Bot: Thanks! I'll remember that next time.")
            save_responses(responses)  # Save the updated responses to the file

        if user_input == "bye":
            print("Bot: Goodbye!")
            break

chatbot() # calling the chatbot function
