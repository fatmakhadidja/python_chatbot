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

![image](https://github.com/user-attachments/assets/375509ff-b942-4313-b764-cc3b850414cb)


## Saving Responses
The bot saves new responses in the responses.json file.<br>
If the bot doesn't know how to respond to a question, it will ask the user for an answer and store it in the file for future use.<br>

# Customizing the Chatbot
You can edit the responses.json file to add new responses. The bot will automatically load these responses when it starts.
The responses are stored in key-value pairs, where the keys are the user inputs, and the values are the bot's replies.

# Contributing
Feel free to fork the repository and submit pull requests if you make improvements or add features. Contributions are welcome!
