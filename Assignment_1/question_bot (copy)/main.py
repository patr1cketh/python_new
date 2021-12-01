import random
from QuestionBot import QuestionBot

# Dictionary of questions and possible answers
questions = {
    1: {
        "question": "",
        "answers": []
        },
    2: {
        "question": "",
        "answers": []
        },
    3: {
        "question": "",
        "answers": []
        },
    4: {
        "question": "",
        "answers": []
        },
    5: {
        "question": "",
        "answers": []
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
            else:
                bot_1.display_incorrect() # If incorrect, calls display_incorrect()
        
        # After all the questions have been answered the goodbye message is set
        bot_1.set_goodbye_message() 
        bot_1.terminate_messsage() # Displays the goodbye message
        quit() # Ends the program

    # If the user does not want to play the bot says goodbye and the program ends           
    if response == "n":
        bot_1.draw()
        print("Goodbye")
        quit()
        