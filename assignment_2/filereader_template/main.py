from filereader import QuestionFileReader
import random

def control_flow():
    response = ""
    while response != "y" or "n":
        response = input("Continue? (y/n) \n")
        if response == "y":
            break
        elif response == "n":
            print("Goodbye.")
            quit()

print("Creating an instance of the QuestionFileReader class...")
qfr_1 = QuestionFileReader("question_bank_2.txt")
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing __str__() method...")
print(qfr_1)
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing get_filename() method...")
print("Filename: ", qfr_1.get_filename())
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing set_filename() method...")
print("Setting filename to 'test.txt'...")
qfr_1.set_filename("test.txt")
print("Filename: ", qfr_1.get_filename())
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing filename property...")
print("Setting filename back to 'question_bank_2.txt'...")
qfr_1.filename = "question_bank_2.txt"
print("Getting filename....")
print("Filename: ", qfr_1.filename)
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing get_line_amount() method...")
print("Total number of lines in file: ", qfr_1.get_line_amount())
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing read_file() method...")
print("Reading the entire contents of the file excluding line 0...")
print(qfr_1.read_file())
print("-\n----\n")
control_flow()
print("\n-----\n")

print("Testing read_random_range() method...")
print("Reading a random range of lines...")
print(qfr_1.read_random_range())
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing get_lines_at() method...")
random_list = random.sample(range(1, qfr_1.get_line_amount()), random.randrange(1, qfr_1.get_line_amount()))
print("Randomly generated list: ", random_list)
print("Passing list into get_lines_at()...")
print(qfr_1.get_lines_at(random_list))
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing all_dictionary_questions() method...")
print("Getting all questions in the file in dictionary format...")
print(qfr_1.all_dictionary_questions())
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing random_dictionary_questions() method...")
print("Getting a random range of questions in dictionary format...")
print(qfr_1.random_dictionary_questions())
print("\n-----\n")
control_flow()
print("\n-----\n")

print("Testing complete.")
print("Goodbye.")
quit()


    