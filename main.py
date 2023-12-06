
import json
import re
import random_responses

# Load JSON data from the specified file
def load_json(file):
    with open(file, 'r') as bot_responses:
        print("Openfabric Chatbot: Greetings. I am Openfabric Chatbot. How can I assist you today?")
        return json.load(bot_responses)

# Store loaded JSON data
response_data = load_json("chat.json")

# Process user input and retrieve an appropriate response
def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Evaluate all available responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if the response contains any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Only consider responses that match the required word count
        if required_score == len(required_words):
            # Check if any of the user's words match the response keywords
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        # Add the calculated score to the list of potential responses
        score_list.append(response_score)

    # Select the highest-scoring response if any responses scored above zero
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Handle empty user input
    if input_string == "":
        return "No input received. Please let me know if you have any questions."

    # Return a random response if no suitable response is found
    if best_response != 0:
        return response_data[response_index]["chatbot_response"]

    return random_responses.random_string()

# Continuously interact with the user until they indicate they want to exit
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Openfabric Chatbot:", get_response(user_input))
