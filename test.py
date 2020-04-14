from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot  = ChatBot('My Bot', storage_adapter = 'chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')


while True:
    message = input("Me : ")
    print(f"Bot: {bot.get_response(message)}")
    