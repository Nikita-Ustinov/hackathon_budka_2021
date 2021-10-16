import requests
from bs4 import BeautifulSoup
from typing import List
import datetime


# vgm_url = 'https://www.cinestar.cz/cz/budejovice/filmy' # 'https://www.visitceskebudejovice.cz/cz/kalendar-akci-ceske-budejovice/2/'
# html_text = requests.get(vgm_url).text
# soup = BeautifulSoup(html_text, 'html.parser')
# print('Done')


class Question:
    def __init__(self, id, text: str, answers: list):
        self.id = id
        self.text = text
        self.answers = answers   

    def get_text(self)->str:
        out = f'{self.text}'
        out += '\n\n'
        for i, a in enumerate(self.answers):
            out += f'{i+1}){a[0]}'
            out += '\n\n'

        return out



class Event:
    def __init__(self, name: str, date: datetime, place: str=None):
        self.name = name
        self.date = date   
        self.place = place   
    

def get_events():
    events = []
    link = CULTURE_URLS[0][0]
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "row event-row clickable-blank"})
    for row in mydivs:
        event_name = row.find_all("h2")[0].text
        content = row.find_all("p")[0].text
        content = row.find_all("p")[0]
        print('1_event')
    print('get_events')

def get_q_by_id(id: int, qs) -> Question:
    output = None
    for question in qs:
        if question.id == id:
            output = question

    return output


def parse_skript(path: str):
    with open(path) as f:
        contents = f.read()
        print(contents)
    contents_1 = contents.split('\n')
    
    def _create_questions(text: str) -> List[Question]:
        question = None
        answers = []
        output = []
        for i, row in enumerate(text): 
            if len(row) == 0:
                continue
            elif row[0] == 'Q':
                if question is not None:
                    output.append(Question(question_id, question, answers))
                    question = None
                    answers = []
                question_id = int(row.split(':')[1].strip()) 
                question = row.split(':')[2].strip()
            elif row[0] == 'O':
                assert question is not None
                try:
                    id = int(row.split(':')[2].strip())
                except ValueError:
                    ids = row.split(':')[2:]
                    id = ''.join(ids)
                answers.append((row.split(':')[1].strip(), id))
        
        output.append(Question(question_id, question, answers))
        question = None
        answers = []

        return output

    
    return _create_questions(contents_1)



# qs = _create_questions(contents_1)

CULTURE_URLS= [
    ('https://www.visitceskebudejovice.cz/cz/kalendar-akci-ceske-budejovice/2/', get_events)
]
if __name__ == '__main__':
    parse_skript('Dialogs/Parkovani.txt')
    # get_events()
    print('Done')