import random
from datetime import datetime

def chatbot():
    responses = {
        "greeting": {
            "keywords": ["hi", "hello", "hey", "yo", "hola"],
            "responses": [
                "Hey there!",
                "Hello! Hope you're doing well!",
                "Hi! Nice to see you."
            ]
        },
        "help": {
            "keywords": ["help", "assist", "support", "need help"],
            "responses": [
                "Sure! What do you need help with?",
                "I'm here to help",
                "Tell me your problem."
            ]
        },
        "time": {
            "keywords": ["time", "clock"],
            "responses": lambda: [
                f"The current time is {datetime.now().strftime('%I:%M:%S %p')}."
            ]
        },
        "date": {
            "keywords": ["date", "today", "day"],
            "responses": lambda: [
                f"Today's date is {datetime.now().strftime('%B %d, %Y')}."
            ]
        },
        "name": {
            "keywords": ["your name", "who are you", "what are you"],
            "responses": [
                "You can call me ChatBot!",
                "I'm a simple Python chatbot."
            ]
        },
        "creator": {
            "keywords": ["creator", "who made you", "developer"],
            "responses": [
                "I was created by https://github.com/aashifm1",
                "A human built me using Python."
            ]
        },
        "how_are_you": {
            "keywords": ["how are you", "how r u", "how you doing"],
            "responses": [
                "I'm doing great! Thanks for asking.",
                "All good here! What about you?"
            ]
        },
        "joke": {
            "keywords": ["joke", "funny", "make me laugh"],
            "responses": [
                "Why do programmers hate nature? Too many bugs.",
                "I told my wife she should embrace her mistakes. She hugged me.",
                "I’m on a seafood diet. I see food and I eat it.",
                "Why don’t skeletons fight each other? They don’t have the guts.",
                "I asked my dog what’s two minus two. He said nothing.",
                "Why did Python break up with Java? Too many classes.",
                "Why don’t eggs tell jokes? They’d crack each other up.",
                "I used to think I was indecisive, but now I’m not too sure.",
                "Why did the scarecrow win an award? Because he was outstanding in his field.",
                "I told my friend 10 jokes to make him laugh. Sadly, no pun in ten did.",
                "Why did the math book look sad? It had too many problems.",
                "I tried to catch fog yesterday. Mist."
            ]
        },
        "thanks": {
            "keywords": ["thanks", "thank you", "thx"],
            "responses": [
                "You're welcome!",
                "No problem at all!",
                "Happy to help!"
            ]
        },
        "morning": {
            "keywords": ["morning", "good morning"],
            "responses": [
                "Good morning!",
                "Morning! Hope today goes well!"
            ]
        },
        "night": {
            "keywords": ["night", "good night"],
            "responses": [
                "Good night!",
                "Sweet dreams!"
            ]
        },
        "bye": {
            "keywords": ["bye", "goodbye", "exit", "quit"],
            "responses": [
                "Goodbye!",
                "See you soon!",
                "Take care!"
            ]
        }
    }


    print("\nChatBot: Hey! This is a chatbot. Type 'bye' to exit.")

    while True:
        chat = input("\nYou: ").lower().strip()

        if chat in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! Have a great day")
            break

        found = False

        for intent in responses.values():
            for keyword in intent["keywords"]:
                if keyword in chat:
                    replies = intent["responses"]
                    if callable(replies): 
                        replies = replies()
                    print("ChatBot:", random.choice(replies))
                    found = True
                    break
            if found:
                break


        if not found:
            print("ChatBot: Sorry. I can't understand what you just said.")

def main():
    chatbot()

if __name__ == "__main__":
    main()
