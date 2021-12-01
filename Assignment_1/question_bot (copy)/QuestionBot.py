import random

class QuestionBot:

    # Dictionary containing a different goodbye message depending on the user's score
    __goodbye_messages = {
    0 : "You scored 0/5! (╥_╥) \nHow embarassing!",
    1 : "You scored 1/5...\nAt least it's not 0! ¯\_(ツ)_/¯ ",
    2 : "You scored 2/5.\nGo do some study and try again!",
    3 : "You scored 3/5.\nNot bad!",
    4 : "You scored 4/5!\nGreat job!! (~‾▿‾)~",
    5 : "You scored 5/5!!\nWow you're a genius!! (ง^ᗜ^)ง"
    }

    # should these be class or instance variables?

    question_number = 1 # Class variable that keeps track of the question number
    __goodbye_message = "" # class variable that stores the goodbye message
    
    def __init__(self, bot_name, questions):
        # instance variables containing bot name, questions and score
        self.__bot_name = bot_name 
        self.__questions = questions
        self.__score = 0

    # This method defines a string representation of the object       
    def __str__(self):
        description = "Bot name: %s \nNumber of questions: %d" % (self.__bot_name, len(self.__questions)) # should there be more here?
        return description
    
    def draw(self):
        print(" [@@] ")
        print("/|__|\\")
        print(" d  b ")

    # The bot greets the user and asks them if they want to play
    def display_name(self):
        print("Hi my name is %s the bot and I will be your host today." % self.__bot_name)
        print("Would you like to play the quiz? (y/n)")

    # To be called when the user selects the correct answer
    def display_correct(self):
        print("Correct! Good job!\n")
        self.__score += 1 # Increment the score
        self.question_number += 1 # Increment the question number

    # To be called when the user selects the incorrect answer
    def display_incorrect(self):
        current_q = self.__questions[self.question_number] # Gets the current question from the questions dictionary
        a = current_q["answers"] # Gets the list of answers
        correct_answer = a[0] # # The variable a contains the list of answers and the correct answer is the first item on the list
        print("Incorrect. The correct answer is %s\n" % correct_answer) 
        self.question_number += 1 # Increment the question number

    # To be called for each question
    def current_question(self):
        current_q = self.__questions[self.question_number] # Gets the current question from the questions dictionary
        q = current_q["question"] # Assigns the question to q
        a = current_q["answers"] # Assigns the list of answers to a
        answers_random = random.sample(a, len(a)) # Randomizes the answers and assigns them to a new list

        #Presents the question and answers to the user
        print("---%s---" % self.__bot_name)
        print("%s" % q)
        print("--------------------------------")
        print("A. %s" % answers_random[0])
        print("B. %s" % answers_random[1])
        print("C. %s" % answers_random[2])
        print("D. %s" % answers_random[3])
        print("--------------------------------")
        print("Please type ypur answer.\n")
                
    # To be called each time the user inputs an answer
    def check_answer(self, response):
        current_q = self.__questions[self.question_number]
        a = current_q["answers"]
        correct_answer = a[0] # The correct answer is always the first item in the list
        # Compare the users response with the correct answer
        if response.lower() == correct_answer.lower(): # Convert both to lowercase to ensure capital letters don't affect answer
            return True
        else:
            return False

    # Allow the user to input new questions?
    def set_questions(self, new_questions):
        if type(new_questions) == dict and type(new_questions[1].value) == dict: # Check if new_questions is in correct format
            self.__questions = new_questions
            self.__questionNumber = 1
        else:
            raise TypeError("Questions in incorrect format")
    
    # Resets the game
    def reset(self):
        self.__questionNumber = 1

    # To be called at the end of the game
    def terminate_messsage(self):
        print(self.get_goodbye_message()) # Gets the goodbye message and prints it
        self.draw() # Draws the robot
        print("The game is now over. Thank you for playing.")
    
    # Gets the score
    def get_score(self):
        return self.__score
        
    # Gets the bot name
    def get_bot_name(self):
        return self.__bot_name

    # Sets the bot name
    def set_bot_name(self, new_name):
        self.__bot_name = new_name

    # Gets the goodbye message
    def get_goodbye_message(self):
        return self.__goodbye_message

    # Sets the goodbye message using the users score
    def set_goodbye_message(self):
        self.__goodbye_message = self.__goodbye_messages[self.get_score()]
