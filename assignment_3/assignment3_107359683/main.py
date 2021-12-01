import random
from Bot import Bot, QuestionBot

# Dictionary of questions and possible answers
questions = {
    1: {
        "question": "What is the capital city of Spain?",
        "answers": ["Madrid","Barcelona","Lisbon","Cork"]
        },
    2: {
        "question": "Hg is the chemical symbol of which element?",
        "answers": ["Mercury","Hydrogen","Helium","Oxygen"]
        },
    3: {
        "question": "Which country produces the most coffee in the world?",
        "answers": ["Brazil","Ireland","Russia","Kenya"]
        },
    4: {
        "question": "In what year was the first ever Wimbledon Championship held?",
        "answers": ['1877', '1777','1977','1677']
        },
    5: {
        "question": "What is Chandler’s last name in the sitcom Friends?",
        "answers": ["Bing","Bong","Boing","Bang"]
        }
}

bot_names = ["Billy", "Bob", "Bailey", "Beatrice"] # List of bot names

# Creates a new instance of the Bot class.
# Passes in a random name from the list of bot names
print("Creating a new instance of the bot class...\n")
bot_1 = Bot(bot_names[random.randrange(len(bot_names))])
print("-----\n")

# Test string representation
print("Testing __str__()...\n")
print(bot_1)
print("-----\n")

# Test name getter method
print("Testing get_name()...\n")
print(bot_1.get_name())
print("-----\n")

# Test name setter method
print("Testing set_name('Paul')...\n")
bot_1.set_name("Paul")
print("-----\n")

# Test name property
print("Testing get name using name property...\n")
print(bot_1.name)
print("-----\n")
print("Testing set name to 'Sarah' using name property...\n")
bot_1.name = "Sarah"
print("-----\n")
print("Getting name again...\n")
print(bot_1.name)
print("-----\n")

# Test draw method
print("Testing draw()...\n")
bot_1.draw()
print("-----\n")

# Test display name method
print("Testing display_name()...\n")
bot_1.display_name()
print("-----\n")

# Create a new instance of the QuestionBot class
print("Creating a new instance of the QuestionBot class...\n")
qbot_1 = QuestionBot(bot_names[random.randrange(len(bot_names))], questions)
print("-----\n")


# Test method overriding for __str__(), draw() and display_name(). Expected different output from the parent class methods
print("Testing __str__()...\n")
print(qbot_1)
print("-----\n")

print("Testing draw()...\n")
qbot_1.draw()
print("-----\n")

print("Testing display_name()...\n")
qbot_1.display_name()
print("-----\n")

# Test display_correct() method
print("Testing display_correct()...\n")
qbot_1.display_correct()
print("-----\n")

# Test display_incorrect() method
print("Testing display_incorrect()...\n")
qbot_1.display_incorrect()
print("-----\n")

# Test current_question() method
print("Testing current_question()...\n")
print(qbot_1.current_question())
print("-----\n")

# Test check_answer() method
print("Testing check_answer() on question 1 with response 'Cork'. Expected return is False\n")
print(qbot_1.check_answer("Cork"))
print("-----\n")
print("Testing check_answer() on question 1 with response 'Madrid'. Expected return is True\n")
print(qbot_1.check_answer("Madrid"))
print("-----\n")
print("Testing case sensitivity with response 'MADrid'. Expected return is True\n")
print(qbot_1.check_answer("MADrid"))
print("-----\n")

# Test set_questions() method
set_questions_tests = [
    "test",
    {},
    {1:""},
    {1: {}},
    {1: {"question": 123, "answers": []}},
    {1: {"question": "test", "answers": "test"}},
    {1: {"question": "test", "answers": [1,2,3]}},
    {1: {"question": "test", "answers": ["answer1", "answer2"]}}
]
print("Testing set_questions() method with a range of possible arguments. Expected return is incorrect format in all tests except the last.\n")
for i in set_questions_tests:
    print("Test:")
    print(i)
    qbot_1.set_questions(i)
    print("-----\n")  

# Test get_questions() method
print("Testing get_questions() method. Expected return is test questions\n")
print(qbot_1.get_questions())
print("-----\n")
    
# Test get_score() method
print("Testing get_score() method. Expected return is 0\n")
print(qbot_1.get_score())
print("-----\n")

# Test increment_score() and dispay_score methods
print("Incrementing score by 1...\n")
qbot_1.increment_score()
print("-----\n")
print("Testing display_score() method. Expected value is 1\n")
qbot_1.display_score()
print("-----\n")

# Test increment_question_number(), get_question_number() methods and reset() methods
print("Getting question number. Expected return is 1\n")
print(qbot_1.get_question_number())
print("-----\n")
print("Incrementing question number...\n")
qbot_1.increment_question_number()
print("-----\n")
print("Getting question number again. Expected return is 2\n")
print(qbot_1.get_question_number())
print("-----\n")
print("Calling reset()...\n")
qbot_1.reset()
print("Getting question number and score. Expected return is 1 and 0\n")
print(qbot_1.get_question_number())
print(qbot_1.get_score())
print("-----\n")

# Test set_goodbye_message() and get_goodbye_message()
print("Setting goodbye message with score 0...\n")
qbot_1.set_goodbye_message()
print("-----\n")
print("Getting goodbye message...")
print(qbot_1.get_goodbye_message())
print("-----\n")

# Test terminate_message()
print("Testing terminate message...\n")
qbot_1.terminate_messsage()
print("-----\n")
print("Testing complete")








        