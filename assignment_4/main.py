import random
from filereader import QuestionFileReader
from Bot import QuestionBot

def control_flow():
    response = ""
    while response != "y" or "n":
        response = input("Continue? (y/n) \n")
        if response == "y":
            break
        elif response == "n":
            print("Goodbye.")
            quit()

# List of bot names
bot_names = ["Billy", "Bob", "Bailey", "Beatrice", "Barney", "Bart", "Barbara", "Bella", "Benny", "Barry", "Bethany", "Brittany"] 

question_file_reader = QuestionFileReader("question_bank_2.txt") # new instance of QuestionFileReader class

questions_set = question_file_reader.random_dictionary_questions() # gets a random set of questions to start

# creates a new instance of the QuestionBot class with a random name and random questions
question_bot = QuestionBot(bot_names[random.randrange(len(bot_names))], questions_set)
question_bot.draw()
question_bot.display_name()
response = ""
# The program will proceed if the user inputs "y" or quit if the user inputs "n"
while response not in ["y", "n"]:
    response = input()
    if response == "y":

        # FEATURE 1: The user is asked if they want to get a new set of questions
        print("A new quiz has been created with %d random questions.\nThere are %d points for each correct answer.\nPress 'c' to continue or if you would like a new set of questions press 'n'\n[n]ew questions\n[c]ontinue\n" % (len(questions_set), question_bot.get_score_increment()))
        while response not in ["n","c"]:
            response = input()
        if response == "n":
            # ask the user how many questions they want in the new set
            print("How many questions would you like for the quiz?\nPlease enter a number between 2 and 15\n")
            response = 0
            while response < 2 or response > 15: # make sure input is between 2 and 15
                try:
                    response = int(input())
                except ValueError: # catch non-numerical input
                    print("Please enter a number between 2 and 15")
                    response = 0
            # call method for getting new questions passing in the number from the user
            questions_set = question_file_reader.get_new_questions(response)
            # set the new questions to the question bot
            question_bot.set_questions(questions_set)
            question_bot.draw()
            print("Starting quiz with %d new questions\n" % len(questions_set))
        else:
            pass

        # This loop will run for each question
        for i in range(len(questions_set)):

            # FEATURE 2: present the option of the score shuffle before the last question
            if i == len(questions_set) - 1:
                question_bot.draw()
                print("Your current score is %d points" % question_bot.get_score())
                print("Up until now there was a maximum of 10 points for each correct answer.")
                print("For the final question, you can take a chance and play the score shuffler.")
                print("With the score shuffler you can get up to 20 points for the last question!")
                print("But be careful! You might get a bad shuffle and lower the points too!")
                print("Would you like to play the score shuffler? (y/n)\n")
                response = ""
                while response not in ["y", "n"]:
                    response = input()
                # if the user chooses yes, call the shuffle score method and display the result
                if response == "y": 
                    question_bot.shuffle_score()
                    question_bot.display_shuffle_result()
                # if they choose no, do nothing
                if response == "n":
                    pass

            print(question_bot.current_question()) # Displays the question
            response = input() # Waits for user response
            if question_bot.check_answer(response) == True: # Checks if the answer is correct
                question_bot.display_correct() # If correct, calls display_correct()
                question_bot.increment_score() # Increments the score
            else:
                question_bot.display_incorrect() # If incorrect, calls display_incorrect()
            question_bot.increment_question_number() # Increments the question number
        
        # After all the questions have been answered the goodbye message is set
        question_bot.set_goodbye_message() 
        question_bot.terminate_messsage() # Displays the goodbye message
        quit() # Ends the program

    # If the user does not want to play the bot says goodbye and the program ends           
    if response == "n":
        question_bot.draw()
        print("Goodbye")
        quit()
        


        



