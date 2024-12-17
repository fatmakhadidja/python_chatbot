# Chatbot Project

A simple Python-based chatbot that can engage in conversation, learn new responses from users, and remember them across sessions.

## Features

- **Predefined Responses**: The bot responds to common questions such as "Hello", "How are you?", etc.
- **Learning Capability**: If the bot doesn't know how to respond, it asks the user for a response and remembers it for future conversations.
- **Persistent Memory**: The bot saves responses in a `responses.json` file, so it remembers user-provided answers even after the program is restarted.
- **Customizable**: You can easily add more responses by editing the `responses.json` file.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/chatbot.git

# Navigate to the project directory:
```bash
 cd chatbot
```
# Run the Python script:
```bash
 python3 chatbot.py
```
or   
```bash
py chatbot.py
```

# Example Interaction
Hello, I'm your chatbot. Type 'bye' to exit.<br>
You: hello<br>
Bot: Hi there! How can I help you?<br>
You: what's your favorite color?<br>
Bot: I like all colors, but if I had to pick, maybe blue? It’s calming!<br>
You: what is your favorite animal?<br>
Bot: I'm not sure how to respond to that.<br>
I don't know that yet. Can you tell me what to say? tiger<br>
Bot: Thanks! I'll remember that next time.<br>
You: bye<br>
Bot: Goodbye!<br>

## Saving Responses
The bot saves new responses in the responses.json file.<br>
If the bot doesn't know how to respond to a question, it will ask the user for an answer and store it in the file for future use.<br>

# Customizing the Chatbot
You can edit the responses.json file to add new responses. The bot will automatically load these responses when it starts.
The responses are stored in key-value pairs, where the keys are the user inputs, and the values are the bot's replies.

# Contributing
Feel free to fork the repository and submit pull requests if you make improvements or add features. Contributions are welcome!
