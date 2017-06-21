import sqlite3
import json

f = open('/Users/sea_fog/Documents/github/Letuchiy_polls/polls.json', 'r', encoding='utf-8')
dicts = json.loads(f.read())
conn = sqlite3.connect('/Users/sea_fog/Documents/github/Letuchiy_polls/answers.db')
c = conn.cursor()
all_questions = []
answers_info = []
n = 1
for d in dicts:
    command = 'CREATE TABLE IF NOT EXISTS question' + str(n) + ' (answer TEXT, frequency INTEGER)'
    c.execute(command)
    n += 1
    for key in d:
        if key == 'question':
            all_questions.append(d[key])
        elif key == 'answers':
            answers_info.append(d[key])
        else:
            continue
all_answers = []
n = 1
for el in answers_info:
    answers = []
    comm = 'INSERT INTO question' + str(n) + ' (answer, frequency) VALUES (?, ?)'
    n += 1
    for d in el:
        for key in d:
            if key == 'text':
                answers.append(d[key])
                c.execute(comm, (d[key], str(0)))
                conn.commit()
            else:
                continue
    all_answers.append(answers)
c.close()
conn.close()