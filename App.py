from flask import Flask, render_template, url_for, request

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
app.debug = True
app.static_folder = 'static'

clownbot = ChatBot('ChatterBot', storage_adapter = 'chatterbot.storage.SQLStorageAdapter')
trainer  = ChatterBotCorpusTrainer(clownbot)
trainer.train('chatterbot.corpus.english', 'chatterbot.corpus.english.greetings')


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/send', methods = ['GET', 'POST'])
def send():
    global clownbot
    if request.method == 'POST': 
        user_query = request.form['message'] # user input message
    return render_template('index.html', response = clownbot.get_response(user_query)  )

if __name__ == "__main__":
    app.run()
