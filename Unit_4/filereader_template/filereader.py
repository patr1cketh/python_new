class FileReader:

    def __init__(self, filename):
        self.__filename = filename
        print("instance of FileReader class created!")
    
    def read_file(self):
        file_contents = []
        with open(self.__filename) as file_1:
            for line in file_1:
                file_contents.append(line)
        return file_contents
    

class QuestionFileReader(FileReader):
    pass