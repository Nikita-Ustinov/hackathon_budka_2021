
from flask import Flask, render_template, request
from Core import parse_skript

app = Flask(__name__)

with open('file.txt','r') as file:
    conversation = file.read()

@app.route("/")
def home(): 
    global parking 
    parking = parse_skript('Dialogs/Parkovani.txt')
	return render_template("home.html")

@app.route("/get")
def get_bot_response():
    global history, q_counter
	
    userText = request.args.get('msg')
    history.append(userText)
    if userText not in TEMA:
        answer = f'Nerozumim odpovedi. Prosim napiste neco ze seznamu: {TEMA}'
    else:
        answer = f'Dekuji, zvolil jste tema {userText}. ' 
        answer += 'Co vas s tim trapi?'

    return answer

q_counter = 0
parking = None
history = []
TEMA = ['Volny cas', 'Parkovani', 'Lekar', 'Urad']
if __name__ == "__main__":
	app.run()