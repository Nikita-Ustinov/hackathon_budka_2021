
from flask import Flask, render_template, request
from Core import parse_skript, get_q_by_id

app = Flask(__name__)

with open('file.txt','r') as file:
    conversation = file.read()

@app.route("/")
def home(): 
	return render_template("home.html")

@app.route("/get")
def get_bot_response():
    global history, q_counter
	
    userText = request.args.get('msg')
    history.append(userText)
    if q_counter == -1:
        if userText not in TEMA:
            answer = f'Nerozumim odpovedi. Prosim napiste neco ze seznamu: {TEMA}'
        else:
            answer = f'Dekuji, zvolil jste tema {userText}. ' 
            answer += 'Co vas s tim trapi?'
        q_counter = 0
    
    if q_counter != -1:
        answer = show_parking_dialog(q_counter, userText)

    return answer

def show_parking_dialog(step: int, userText):
    output = None
    try:
        userText = int(userText)
        print(f'S: {step}, userText is int')
    except ValueError:
        print(f'S: {step}, userText is text')
    if step == -1:
        output = parking[0].text
    else:
        answers = parking[step].answers
        good_answer = False
        for answer in answers:
            if type(userText) == int:
                if answer[1] == userText:
                    good_answer = True
            elif answer[0] == userText:
                good_answer = True

            if not good_answer:
                output = f'Prosim zadejte jednu z predefinovanych odpovedi: {answers}'  
            else:
                step += 1
                output = get_q_by_id(step)
    return output


q_counter = -1
history = []
parking = parse_skript('Dialogs/Parkovani.txt')
TEMA = ['Volny cas', 'Parkovani', 'Lekar', 'Urad']
if __name__ == "__main__":
	app.run()