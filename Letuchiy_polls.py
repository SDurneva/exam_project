from flask import Flask,render_template,request
import json
import os
import filesort
import re

app = Flask(__name__,static_url_path='/Users/sea_fog/Documents/github/Letuchiy_polls/static',
            static_folder='/Users/sea_fog/Documents/github/Letuchiy_polls/static')
filename = 'data.txt'


@app.route('/')
def main_page():
    f = open('/Users/sea_fog/Documents/github/Letuchiy_polls/polls.json', 'r', encoding='utf-8')
    dicts = json.loads(f.read())
    all_questions = []
    answers_info = []
    for d in dicts:
        for key in d:
            if key == 'question':
                all_questions.append(d[key])
            elif key == 'answers':
                answers_info.append(d[key])
            else:
                continue
    all_answers = []
    for el in answers_info:
        answers = []
        for d in el:
            for key in d:
                if key == 'text':
                    answers.append(d[key])
                else:
                    continue
        all_answers.append(answers)
    return render_template('main_page.html', all_questions=all_questions, all_answers=all_answers)

@app.route('/stats')
def stats():
    f = open('/Users/sea_fog/Documents/github/Letuchiy_polls/polls.json', 'r', encoding='utf-8')
    dicts = json.loads(f.read())
    all_questions = []
    answers_info = []
    for d in dicts:
        for key in d:
            if key == 'question':
                all_questions.append(d[key])
            elif key == 'answers':
                answers_info.append(d[key])
            else:
                continue
    all_answers = []
    for el in answers_info:
        answers = []
        for d in el:
            for key in d:
                if key == 'text':
                    answers.append(d[key])
                else:
                    continue
        all_answers.append(answers)
    if request.args:
        answ1 = request.args.get('answ1')
        answ2 = request.args.get('answ2')
        answ3 = request.args.get('answ3')
        answ4 = request.args.get('answ4')
        answ5 = request.args.get('answ5')
        answ6 = request.args.get('answ6')
        answ7 = request.args.get('answ7')
        answ8 = request.args.get('answ8')
        answ9 = request.args.get('answ9')
        answ10 = request.args.get('answ10')
        answ11 = request.args.get('answ11')
        answ12 = request.args.get('answ12')
        answ13 = request.args.get('answ13')
        answ14 = request.args.get('answ14')
        answ15 = request.args.get('answ15')
        answ16 = request.args.get('answ16')
        answ17 = request.args.get('answ17')
        answ18 = request.args.get('answ18')
        answ19 = request.args.get('answ19')
        answ20 = request.args.get('answ20')
        answ21 = request.args.get('answ21')
        answ22 = request.args.get('answ22')
        answ23 = request.args.get('answ23')
        answ24 = request.args.get('answ24')
        answ25 = request.args.get('answ25')
        answ26 = request.args.get('answ26')
        answ27 = request.args.get('answ27')
        answ28 = request.args.get('answ28')
        answ29 = request.args.get('answ29')
        answs = [answ1, answ2, answ3, answ4, answ5, answ6, answ7, answ8, answ9, answ10, answ11, answ12, answ13,
                 answ14, answ15, answ16, answ17, answ18, answ19, answ20, answ21, answ22, answ23, answ24, answ25, answ26,
                 answ27, answ28, answ29]
        dir = '/Users/sea_fog/Documents/github/Letuchiy_polls/results/'
        i = 1
        for answ in answs:
            filename = dir + 'chapt' + str(i) + '.txt'
            with open(filename, 'a', encoding='utf-8') as file:
                try:
                    file.write(answ)
                    i += 1
                except:
                    print('Печалька с файлом %s' % filename)
        print(os.listdir(dir))
        files = filesort.sortfiles(os.listdir(dir))
        print(files)
        answers_stats = []
        for file in files:
            answs_stats = []
            f = open(dir + file, 'r', encoding='utf-8')
            a = f.read()
            for i in range(1,9):
                answs_stats.append(a.count(str(i)))
            answers_stats.append(answs_stats)
    return render_template('stats.html', answers_stats=answers_stats, all_questions=all_questions)




if __name__ == '__main__':
    app.run()
