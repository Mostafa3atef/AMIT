from QUIZ import Quiz  

questions = [
    {
        'question': 'How many hours are there in a day?',
        'answers': ['18', '24', '12', '06'],
        'correct_answer': '24'
    },
    {
        'question': 'How many letters are there in the English alphabet?',
        'answers': ['25', '27', '26', '28'],
        'correct_answer': '26'
    },
    {
        'question': 'Name the house made of ice?',
        'answers': ['Cave', 'Home', 'Igloo', 'Apartment'],
        'correct_answer': 'Igloo'
    },
    {
        'question': 'How many days in a week',
        'answers': ['6', '7', '8', '9'],
        'correct_answer': '7'
    },
    {
        'question': 'How many days in a year',
        'answers': ['361', '363', '365', '367'],
        'correct_answer': '365'
    },
]

quiz= Quiz()
x=0
for x in questions:
    print('\n',x['question'])
    get_answers= quiz.quiz_answers(x['answers'])
    checking= quiz.check(x['correct_answer'],get_answers)

quiz.final_result()