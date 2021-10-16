import requests
from bs4 import BeautifulSoup
from typing import List


# vgm_url = 'https://www.cinestar.cz/cz/budejovice/filmy' # 'https://www.visitceskebudejovice.cz/cz/kalendar-akci-ceske-budejovice/2/'
# html_text = requests.get(vgm_url).text
# soup = BeautifulSoup(html_text, 'html.parser')
# print('Done')



def get_events():
    events = []
    link = CULTURE_URLS[0][0]
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "row event-row clickable-blank"})
    for row in mydivs:
        evnet_name = row.find_all("h2")[0].text
        content = row.find_all("p")[0].text
        content = row.find_all("p")[0]
        print('1_event')
    print('get_events')


def parse_skript(path: str):
    with open(path) as f:
        contents = f.read()
        print(contents)
    contents_1 = contents.split('\n')
    
    def _create_questions(text: str) -> List[Question]:
        question = None
        answers = []
        output = []
        # print(text)
        for i, row in enumerate(text): 
            # print(f'Row_id: {i}, row: {row}')
            if len(row) == 0:
                continue
            elif row[0] == 'Q':
                print(f'1')
                if question is not None:
                    print(f'New Q')
                    output.append(Question(question_id, question, answers))
                    question = None
                    answers = []
                print(row.split(':'))
                question_id = row.split(':')[1].strip()
                question = row.split(':')[2].strip()
            elif row[0] == 'O':
                print(f'2')
                assert question is not None
                answers.append((row.split(':')[1].strip(), row.split(':')[2].strip()))

        return output

    qs = _create_questions(contents_1)
    print('asd')


class Question:
    def __init__(self, id, text: str, answers: list):
        self.id = id
        self.text = text
        self.answers = answers   

# qs = _create_questions(contents_1)

CULTURE_URLS= [
    ('https://www.visitceskebudejovice.cz/cz/kalendar-akci-ceske-budejovice/2/', get_events)
]
if __name__ == '__main__':
    parse_skript('Dialogs/Parkovani.txt')
    # get_events()
    print('Done')