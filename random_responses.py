import random


def random_string():
    """Generates a random response when the user's input is not understood."""

    random_list = [
        "I do not understand what you asked for, please be more specific or rephrase your question.",
        "What?",
        "Try again, I don't understand.",
    ]

    # Generates a random index within the range of the random_list
    random_item = random.randrange(len(random_list))

    # Selects the corresponding response from the random_list
    response = random_list[random_item]

    # Returns the selected response
    return response
