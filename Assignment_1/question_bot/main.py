import random
from QuestionBot import QuestionBot

# Dictionary of questions and possible answers
questions = {
    1: {
        "question": "In what year was the first ever Wimbledon Championship held?",
        "answers": ['1877', '1777','1977','1677']
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
        "question": "What is the capital city of Spain?",
        "answers": ["Madrid","Barcelona","Lisbon","Cork"]
        },
    5: {
        "question": "What is Chandler’s last name in the sitcom Friends?",
        "answers": ["Bing","Bong","Boing","Bang"]
        }
}

bot_names = ["Billy", "Bob", "Barry"] # List of bot names

# Creates a new instance of the QuestionBot class.
# Passes in a random name from the list of bot names and the questions dictionary
bot_1 = QuestionBot(bot_names[random.randrange(len(bot_names))], questions)

# Test string representation
#print(new_bot)

# Draws the bot, displays the greeting to the user and waits for a response
bot_1.draw()
bot_1.display_name()
response = ""

# The program will proceed if the user inputs "y" or quit if the user inputs "n"
while response != "y" or "n":
    response = input()
    if response == "y":

        # This loop will run for each question in the questions dictionary
        for i in range(len(questions)):
            bot_1.current_question() # Displays the question
            response = input() # Waits for user response
            if bot_1.check_answer(response) == True: # Checks if the answer is correct
                bot_1.display_correct() # If correct, calls display_correct()
                bot_1.increment_score() # Increments the score
            else:
                bot_1.display_incorrect() # If incorrect, calls display_incorrect()
            bot_1.increment_question_number() # Increments the question number
        
        # After all the questions have been answered the goodbye message is set
        bot_1.set_goodbye_message() 
        bot_1.terminate_messsage() # Displays the goodbye message
        quit() # Ends the program

    # If the user does not want to play the bot says goodbye and the program ends           
    if response == "n":
        bot_1.draw()
        print("Goodbye")
        quit()
        