
def current_question(question):
    q = question["question"]
    a = question["answers"]
    return q, a

questions = {
    1: {
        "question": "Which countries do cities of Perth, Adelade & Brisbane belong to?",
        "answers": ['Australia', 'Austria','USA','Finland']
        },
    2: {
        "question": "How many languages are written from right to left?",
        "answers": ["12","11","3","4"]
        },
    3: {
        "question": "How long is an Olympic swimming pool (in metres)?",
        "answers": ["50 metres","40 metres","80 metres","30 metres"]
        },
    4: {
        "question": "From which country does Gouda cheese originate?",
        "answers": ["Netherlands","Belgium","France","Germany"]
        },
    5: {
        "question": "What was the first soft drink in space?",
        "answers": ["Coca Cola","7up","Fanta","Pepsi"]
        }
}

num_of_questions = 5

for i in range(1, num_of_questions + 1):
    current_q = questions[i]
    print(current_question(current_q))
