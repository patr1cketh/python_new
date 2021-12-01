import random

class Bot:

    # constructor method is called each time an instance of this class is created
    def __init__(self, name):
        self.__botname = name # name is an instance variable because this will change for each instance
    
    # this method returns a readable describtion of the object
    def __str__(self):
        description = "This is an instance of the Bot class.\nThe Bot class is a parent class which contains methods for displaying the bot's name and drawing the bot.\nThe name of this instance is %s" % self.__botname
        return description
    
    # getter for name
    def get_name(self):
        return self.__botname
    
    # setter for name
    def set_name(self, name):
        self.__botname = name
    
    name = property(get_name, set_name) # property for name

    # The bot greets the user and states their name
    def display_name(self):
        print("Hi my name is %s the bot" % self.__botname)
    
    # Draws the bot
    def draw(self):
        print(" [@@] ")
        print("/|__|\\")
        print(" d  b ")

class QuestionBot(Bot): # QuestionBot is a child class of Bot
    
    def __init__(self, name, questions):
        # We call __init__() from the parent class and pass it name
        super().__init__(name)
        # We add these instance variables here because they are specific to the child class
        self.__score = 0 # initialise score to 0
        self.__score_increment = 10 # Initalises the score increment to 10
        self.__question_number = 1 # Initialises the question number to 1
        self.__goodbye_message = "" # Initalises goodbye message to an empty string
        self.__questions = questions # Assigns the questions variable passed in to self.__questions
        self.__percentage = 0 # initailise percentage to 0
    
    # This method will override the __str__() method from the parent class.      
    def __str__(self):
        description = "This is an instance of the QuestionBot class.\nQuestionBot is a child class of Bot. It contains additional attributes and methods that allow it to be a host of a trivia game.\nThe name of this instance is %s" % super().get_name()
        return description
    
    # This method will override the display_name() method from the parent class 
    def display_name(self):
        print("Hi my name is %s the bot and I will be your host today." % super().get_name())
        print("Would you like to play the quiz? (y/n)")
    
    # This method will override the draw() method from the parent class
    def draw(self):
        print("  \\/")
        print(" [oo] ")
        print("/|__|\\")
        print(" _||_ ")
    
    # Gets the score
    def get_score(self):
        return self.__score

    # Increments the score
    def increment_score(self):
        self.__score += self.__score_increment
    
    # Get score increment
    def get_score_increment(self):
        return self.__score_increment

    # Display's the score
    def display_score(self):
        print("Your current score is %d" % self.__score)
    
     # Increments the question number
    def increment_question_number(self):
        self.__question_number += 1
    
    # Getter for question number
    def get_question_number(self):
        return self.__question_number
    
    # Resets the game
    def reset(self):
        self.__question_number = 1
        self.__score = 0
    
    # Getter method for questions
    def get_questions(self):
        return self.__questions

    # To be called when the user selects the correct answer
    def display_correct(self):
        print("Correct! %d points!\n" % self.get_score_increment())

    # To be called when the user selects the incorrect answer
    def display_incorrect(self):
        current_q = self.__questions[self.__question_number] # Gets the current question from the questions dictionary
        a = current_q["answers"] # Gets the list of answers
        correct_answer = a[0] # The variable a contains the list of answers and the correct answer is the first item on the list
        print("Incorrect. The correct answer is %s\n" % correct_answer) 

    # To be called for each question
    def current_question(self):
        current_q = self.__questions[self.__question_number] # Gets the current question from the questions dictionary
        q = current_q["question"] # Assigns the question to q
        a = current_q["answers"] # Assigns the list of answers to a
        answers_random = random.sample(a, len(a)) # Randomizes the answers and assigns them to a new list

        #Presents the question and answers to the user
        q_and_a = "---%s---\n%s\n-----\nA. %s\nB. %s\nC. %s\nD. %s\n-----\nPlease type your answer.\n" % (self.name, q, answers_random[0], answers_random[1], answers_random[2], answers_random[3])
        return q_and_a
                
    # To be called each time the user inputs an answer
    def check_answer(self, response):
        current_q = self.__questions[self.__question_number]
        a = current_q["answers"]
        correct_answer = a[0] # The correct answer is always the first item in the list
        # Compare the users response with the correct answer
        if response.lower() == correct_answer.lower(): # Convert both to lowercase to ensure capital letters don't affect answer
            return True
        else:
            return False

    # Sets new questions only if the variable passed in is in the correct format
    def set_questions(self, new_questions):
        correct_format = True
        if new_questions == {}: # An empty dictionary was not getting caught in my checks below so I added this condition at the start
            correct_format = False
        elif type(new_questions) == dict: # Check that variable is a dictionary
            for i in new_questions.keys(): # Check that all keys are integers
                if type(i) == int:
                    if type(new_questions[i]) == dict and new_questions[i] != {}: # Check that all values are dictionarys and check for edge case of empty dictionary
                        inner_dict_keys = list(new_questions[i].keys()) # Create a list containing the keys of the inner dictionary
                        if inner_dict_keys[0] == "question" and inner_dict_keys[1] == "answers": # Check that the first key is "question" and the second key is "answers"
                            if type(new_questions[i]["question"]) == str: # Check the the value for "question" is a string
                                if type(new_questions[i]["answers"]) == list: # Check that the value for "answers" is a list
                                    for j in new_questions[i]["answers"]: # Check that all the elements in the answers list are strings
                                        if type(j) == str:
                                            pass # If all checks pass, do nothing
                                        else:
                                            correct_format = False # If any of the checks fail, set correct_format to False
                                else:
                                    correct_format = False
                            else:
                                correct_format = False
                        else:
                            correct_format = False
                    else:
                        correct_format = False
                else:
                    correct_format = False
        else:
            correct_format = False
        
        # Set the self.__questions variable if the parameter is in the correct format
        try:
            if correct_format == True:
                self.__questions = new_questions
                print("New questions set succesfully\n")
            else:
                raise TypeError
        
        # If there is a TypeError, display a message to the user
        except:
            print("Questions in incorrect format")
    
    # Gets the goodbye message
    def get_goodbye_message(self):
        return self.__goodbye_message

    # Sets the goodbye message using the users score
    def set_goodbye_message(self):
        max_points = (len(self.get_questions())) * 10 # 10 points for each question
        self.__percentage = (self.get_score()/max_points) * 100
        
        # display different messages depending on score
        if self.__percentage == 0:
            self.__goodbye_message = "You scored 0 points! (╥_╥) \nHow embarassing!" 
        elif self.__percentage > 0 and self.__percentage <= 20:
            self.__goodbye_message = "You scored %d/%d points...\nAt least it's not 0! ¯\_(ツ)_/¯ " % (self.get_score(), max_points)
        elif self.__percentage > 20 and self.__percentage <= 40:
            self.__goodbye_message = "You scored %d/%d points.\nGo do some study and try again!" % (self.get_score(), max_points)
        elif self.__percentage > 40 and self.__percentage <= 60:
            self.__goodbye_message = "You scored %d/%d points.\nNot bad!" % (self.get_score(), max_points)
        elif self.__percentage > 60 and self.__percentage <= 80:
            self.__goodbye_message = "You scored %d/%d points!\nGreat job!! (~‾▿‾)~" % (self.get_score(), max_points)
        elif self.__percentage > 80 and self.__percentage <=100:
            self.__goodbye_message = "You scored %d/%d points!!\nWow you're a genius!! (ง^ᗜ^)ง" % (self.get_score(), max_points)
        else:
            self.__goodbye_message = "WOAH You scored %d/%d points!!\nHow is that even possible??\nMaybe it was something to do with the score shuffler..? ¯\_(ツ)_/¯\nGreat Job!" % (self.get_score(), max_points)
    
    # To be called at the end of the game
    def terminate_messsage(self):
        print(self.get_goodbye_message()) # Gets the goodbye message and prints it
        self.draw() # Draws the robot
        print("The game is now over. Thank you for playing.")
    
    # FEATURE 2: This method is called if the user choose the score shuffle option for the final question
    def shuffle_score(self):
        print("Shuffling score...")
        multiplier = random.uniform(0,2)
        self.__score_increment = int(self.__score_increment * multiplier)
    
    # displays the result of the score shuffle
    def display_shuffle_result(self):
        print("""
               (( _______
     _______     /\O    O\\
    /O     /\   /  \      \\
   /   O  /O \ / O  \O____O\ ))
((/_____O/    \\\    /O     /
  \O    O\    / \  /   O  /
   \O    O\ O/   \/_____O/
    \O____O\/ ))          ))
  ((
  """)
        if self.__score_increment > 10:
            print("Yay! You won the score shuffle and you can score %d points for the final question!" % self.__score_increment)
        elif self.__score_increment < 10:
            print("Bad luck! You lost the score shuffle now can only get %d points for the final question." % self.__score_increment)
        elif self.__score_increment == 10:
            print("Oops! We shuffled the score but nothing happened!. The max score for the final question is still %d points." % self.__score_increment)




