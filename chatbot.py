
import json
import re
from pathlib import Path

# Load FAQ dataset
BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "faq.json"


def load_faq():
    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data.get("greetings"), list):
            raise ValueError("Invalid greetings data")

        if not isinstance(data.get("faqs"), list):
            raise ValueError("Invalid FAQ data")

        return data

    except FileNotFoundError:
        print("Error: faq.json file not found!")
        return None

    except (json.JSONDecodeError, ValueError) as error:
        print("Error loading FAQ dataset:", error)
        return None


# Identify different user intents
INTENT_PATTERNS = {
    "hours": r"\b(hours?|operation|open|close|working|timings?|schedule)\b",

    "submission": r"\b(submit|submission|internship|project|github|repository|workspace)\b",

    "certificate": r"\b(certificate|certification|receive|issued|issue)\b"
}


def normalize_input(user_input):
    return re.sub(r"\s+", " ", user_input.lower()).strip()


def get_greeting_response(message, greetings):
    for greeting in greetings:
        pattern = r"\b" + re.escape(greeting.lower()) + r"\b"

        if re.search(pattern, message):
            return "Hello! Welcome to Datheon Assistant. How can I help you?"

    return None


def identify_intents(message):
    detected_intents = []

    for intent, pattern in INTENT_PATTERNS.items():
        if re.search(pattern, message):
            detected_intents.append(intent)

    return detected_intents


def get_faq_response(intents, faqs):

    responses = []

    for intent in intents:

        for faq in faqs:

            question = faq["question"].lower()

            if intent == "hours" and (
                "hours" in question or "operation" in question
            ):
                responses.append(faq["answer"])
                break

            elif intent == "submission" and (
                "submit" in question or "project" in question
            ):
                responses.append(faq["answer"])
                break

            elif intent == "certificate" and (
                "certificate" in question
            ):
                responses.append(faq["answer"])
                break

    return responses


def chatbot():

    data = load_faq()

    if data is None:
        return

    greetings = data["greetings"]
    faqs = data["faqs"]

    print("\n====================================")
    print("       DATHEON CHATBOT")
    print("====================================")
    print("Hello! Welcome to Datheon Assistant.")
    print("Ask me about working hours, projects,")
    print("internship submissions and certificates.")
    print("Type 'bye', 'exit' or 'quit' to stop.")
    print("------------------------------------")

    while True:

        try:
            user_input = input("\nYou: ")

            message = normalize_input(user_input)

            if not message:
                print("Bot: Please enter a valid message.")
                continue

            # Exit commands
            if re.fullmatch(r"(bye|exit|quit)", message):
                print("Bot: Thank you for chatting! Goodbye!")
                break

            # Greeting detection
            greeting = get_greeting_response(
                message, greetings
            )

            if greeting:
                print("Bot:", greeting)

            # Multi-intent recognition
            intents = identify_intents(message)

            if intents:

                responses = get_faq_response(
                    intents, faqs
                )

                for response in responses:
                    print("\nBot:", response)

            elif not greeting:

                print(
                    "Bot: Sorry, I couldn't understand "
                    "your question. Please ask about "
                    "business hours, project submission "
                    "or certificates."
                )

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Chat session ended. Goodbye!")
            break

        except Exception as error:
            print("Bot: Something went wrong:", error)


if __name__ == "__main__":
    chatbot()
