from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import menu
from cpuinfo import get_cpu_info
import psutil

'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

bot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    'chatterbot.corpus.custom'
)

# Now let's get a response to a greeting
def searchvaluefunc():
    searchvalue = input()
    response = bot.get_response(searchvalue)
    print(response, "\n")
    while True:
        try:
            searchvaluefuncmenu = int(input("Type 1 to search again or press enter to go back."))
        except ValueError:
            menu.cls()
            menu.mainMenu()
        else:
            break
    if searchvaluefuncmenu == 1:
        menu.cls()
        print("Type something to search.")
        searchvaluefunc()

searchvaluefunc()