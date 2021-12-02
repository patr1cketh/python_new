import random

class FileReader:

    # this method is called each time an instance of the class is created
    def __init__(self, filename):
        self.__filename = filename
    
    # getter for filename
    def get_filename(self):
        return self.__filename
    
    # setter for filename
    def set_filename(self, filename):
        self.__filename = filename
    
    filename = property(get_filename, set_filename) # filename property which will be used to call getter and setter methods

    # counts the number of lines in the file and returns as an int
    # note that this value will be 1 more than the amount of questions because of the header line
    def get_line_amount(self):
            with open(self.__filename) as f: 
                num_of_lines = 0 # counter variable
                for line in f:
                    num_of_lines += 1 # add 1 to the counter for each line
            return num_of_lines

    # reads the entire contents of the file and returns as a string
    def read_file(self):
        with open(self.filename) as f: # file automatically closes at the end of with statement
            file_as_string = f.read() # get the entire contents of the file as string
            file_as_list = file_as_string.splitlines(keepends = True) # split the string into a list of lines preserving the \n
            file_as_list.pop(0) # remove the first element in the list to get rid of the header line
            file_as_string = "".join(file_as_list) # convert back to string
        return file_as_string
    
    # picks 2 random line numbers and returns all the questions in that range
    def read_random_range(self):
        start = 0
        end = 0
        # keep running randint on both variables until the conditions are met
        # the other conditions are accounted for in the parameters for randint()
        while start == end or start > end:
            # start lower limit is 1 because 0 would reference the header line
            # upper limit should be 1 less than the amount of questions so we use get_line_amount - 2
            start = random.randint(1, self.get_line_amount() - 2) 
            
            # end lower limit is 2 because the minimum range will be questions 1-2
            # upper limit should be the last question so we use get_line_amount - 1
            end = random.randint(2, self.get_line_amount() - 1)
        with open(self.filename) as f:
            file_as_string = f.read()
            file_as_list = file_as_string.splitlines(keepends = True)
            # use start and end variables to slice the list of questions. +1 to end because we want the end question number to be included
            random_as_list = file_as_list[start:end + 1] 
            random_as_string = "".join(random_as_list)
        return random_as_string

    # takes in a list of numbers and returns the lines at those numbers
    def get_lines_at(self, line_nums_list):
        lines_as_string = ""
        with open(self.filename) as f:
            file_as_string = f.read()
            file_as_list = file_as_string.splitlines(keepends = True)
            # nested for loops to compare each item in the list to each line in the file
            for line_num in line_nums_list: # loop through the list of line nums
                for line in file_as_list: # loop through the list of lines
                    # check if the line num matches the index of the line. Line numbers will match index number because the 0th index is the header line
                    if line_num == file_as_list.index(line):
                        lines_as_string += line # if it is a match, append the line to the return string
        return lines_as_string               

class QuestionFileReader(FileReader):
    # child class inherits __init__() form parent class

    # returns a string representation of the instance
    def __str__(self):
        description = "This is an instance of the QuestionFileReader class.\nIt is a child class of FileReader.\nIt reads questions from %s" % self.filename
        return description
    
    # uses the read_file() method in the parent class and returns the questions in dictionary format
    def all_dictionary_questions(self):
        file_as_string = self.read_file() # using method defined in the parent class to get all questions as string
        file_as_list = file_as_string.splitlines()
        file_as_dict = {}
        for line in file_as_list:
            line_as_list = line.split(",")
            file_as_dict[int(line_as_list[0])] = { # question number is always at index 0
                    "question":line_as_list[1], # question is always at index 1
                    "answers":line_as_list[2:] # answers are all the remaining elements of the list
                }
        return file_as_dict

    # uses the read_random_range() method in the parent class and returns the questions in dictionary format
    def random_dictionary_questions(self):
        random_as_string = self.read_random_range() # using the method defined in the parent class to get random lines
        random_as_list = random_as_string.splitlines()
        random_as_dict = {}
        question_number = 1 # hardcoding question numbers instead of using the number from the file
        for line in random_as_list:
            line_as_list = line.split(",")
            random_as_dict[question_number] = {
                    "question":line_as_list[1],
                    "answers":line_as_list[2:]
                }
            question_number += 1 # increment the question number for the next iteration
        return random_as_dict

    # FEATURE 1: The user has the option to choose the amount of questions they want at the start of the game
    #            This method gets a new set of questions with the number input by the user
    def get_new_questions(self, num_of_questions): 
        all_questions = self.all_dictionary_questions()
        questions_as_list = list(all_questions.values()) # creates a list question dictionarys
        new_questions = {}
        for question_number in range(1, num_of_questions + 1): # repeats for the number of questions
            new_questions[question_number] = random.choice(questions_as_list) # populates the new dictionary with a random question.
        return new_questions
    
    