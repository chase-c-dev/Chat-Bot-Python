# Plan
# Integrate with Flask and Host as API on Heroku

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Intializes Bot With Name
bot = ChatBot("Chase")

# Sets Storage and Logic Adapters for Bot
bot = ChatBot(
    'Chase',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
      logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Main Trainer For The Bot
maintrainer = ChatterBotCorpusTrainer(bot)
maintrainer.train("chatterbot.corpus.english") 

# Runs The Bot
def botrunner(answer):
    chatstart()
    while True:
        try:
            user_input = answer
            bot_response = bot.get_response(user_input)
            if bot_response.confidence < .2:
                return "Sorry I do not Understand That"
            else:
                return bot_response
        except(KeyboardInterrupt, EOFError, SystemExit):
            break


# Trains the Chatbot
def chatstart():
    conversation = [
        # First portion of each line is user input, second portion is the bots response
        "Hello", "Hi there!",

        "How are you doing?", "I'm doing great.",

        "Thank you.", "You're welcome.",

        "What is your favorite color?", "Green.",

        "What is your favorite food?", "Cheese Burgers",

        "What is your favorite drink?", "Root Beer",

        "What is your favorite hobby?", "I like coding and playing videogames",

        "What is your favorite past time?", "I like coding and playing videogames",

        "What is your favorite activity?", "I like to swim and workout at the gym",

        "How old are you?", "nineteen",

    ]

    trainer = ListTrainer(bot)

    trainer.train(conversation)

# Function Run Section