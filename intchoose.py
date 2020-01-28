from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import menu
from cpuinfo import get_cpu_info
import psutil

def cpuinfo():
    print("CPU Model:\n")
    print(get_cpu_info()["brand"])
    print(psutil.cpu_count(logical=False), "Cores")
    print(psutil.cpu_count(logical=True), "Threads\n")

# Create a new instance of a ChatBot
bot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.25
        }
    ]
)

trainer = ListTrainer(bot)

# Train the chat bot with a few responses
trainer.train([
    'Cpu specs',
    '1 --> '
])

# Get a response for some unexpected input
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


