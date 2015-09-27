#!/usr/bin/env python

from chatterbot import ChatBot

chatbot = ChatBot("Xiao Yuan")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.train(conversation)

response = chatbot.get_response("Good morning!")

# print(response)
