class FileManager:

    def __init__(self, filename):
        self.__path = filename

    def get_line_number(self, line_num):
        file1 = open(self.__path, "r")
        line_pos = 0
        line_to_return = ""

        for line in file1:
            if line_pos == line_num:
                line_to_return = line
            line_pos = line_pos + 1
        line_to_return = line_to_return[:-1]
        file1.close()
        return line_to_return


class ThesaurusFileManager(FileManager):

    def get_line_number_dict(self, line_num):
        
        dictionary_line = {}
        # self.__path and super().__path not working here
        with open("thesaurusfilemanager.txt") as f:
            line_position = 0
            file_line = ""
            for line in f:
                if line_position == line_num:
                    file_line = line
                    break
                line_position += 1
        file_line_as_list = file_line.split(",")
        dictionary_line[file_line_as_list[0]] = file_line_as_list[1:]    
             
        return dictionary_line
        
