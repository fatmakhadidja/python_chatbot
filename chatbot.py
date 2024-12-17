import json
import os
from fuzzywuzzy import process

# Define the default responses
default_responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! How can I assist you today?",
    "hey": "Hey there! What can I do for you?",
    "how are you?": "I'm doing great, thank you for asking!",
    "how's it going?": "I'm good, thanks! How about you?",
    "what's up?": "Not much, just here to chat! How about you?",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Farewell! It was nice chatting with you.",
    "what is your name?": "I'm Chatbot, your virtual assistant.",
    "how can you help me?": "I can answer questions, have conversations, and more!",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "tell me a story": "Once upon a time, there was a chatbot who loved to chat all day long!",
    "what is the weather like?": "I’m not sure about the weather, but it’s always sunny in chatbot land!",
    "what is your favorite color?": "I like all colors, but if I had to pick, maybe blue? It’s calming!",
    "do you know programming?": "Yes, I know Python, Java, and many other languages!",
    "who created you?": "I was created by a team of awesome developers!",
    "what can you do?": "I can chat with you, tell jokes, and even learn new things from our conversation!",
    "how old are you?": "I don't have an age like humans, but I’m always learning new things!",
    "are you a robot?": "I’m a chatbot, not exactly a robot, but I can still help you with all sorts of things.",
    "default": "I'm not sure how to respond to that."
}

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
        
        # Find the best match to the user's input using fuzzywuzzy
        best_match = process.extractOne(user_input, responses.keys())

        if best_match[1] >= 80:  # The threshold for similarity, adjust as needed
            print(f"Bot: {responses[best_match[0]]}")
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
