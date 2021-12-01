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
