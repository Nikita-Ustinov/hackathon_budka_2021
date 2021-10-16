
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
    if q_counter == -2:
        if userText not in TEMA:
            answer = f'Nerozumim odpovedi. Prosim napiste neco ze seznamu: {TEMA}'
        else:
            answer = f'Dekuji, zvolil jste tema {userText}. ' 
            answer += 'Co vas s tim trapi?'
            q_counter = -1
    
    if q_counter >= -1:
        answer, q_counter = show_parking_dialog(q_counter, userText)

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
        step = 0
    else:
        answers = get_q_by_id(step, parking).answers
        good_answer = False
        for answer in answers:
            if type(userText) == int:
                if len(answers) >= userText:
                    good_answer = True
                    curr_answer = answers[userText]
            elif answer[0] == userText:
                good_answer = True
                curr_answer = answer

            if not good_answer:
                output = f'Prosim zadejte jednu z predefinovanych odpovedi: {answers}'  
            else:
                try:
                    new_id = int(curr_answer[1])
                    qu = get_q_by_id(new_id, parking)
                except ValueError:
                    qu = parking[0]
                    step = -2
                    
                if step != -2:
                    output = qu.get_text()
                    step = qu.id
                else:
                    output = curr_answer[0] + curr_answer[1]
                break
    
    return output, step


q_counter = -2
history = []
parking = parse_skript('Dialogs/Parkovani.txt')
TEMA = ['Volny cas', 'Parkovani', 'Lekar', 'Urad']
if __name__ == "__main__":
	app.run()