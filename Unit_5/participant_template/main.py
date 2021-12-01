class Participant:
    def __init__(self, fname, lname):
        self.__first_name = fname
        self.__last_name = lname
    
    def get_fullname(self):
        return self.__first_name + self.__last_name
    
    def set_fullname(self, fullname):
        name_as_list = fullname.split(" ")
        self.__first_name = name_as_list[0]
        self.__last_name = name_as_list[1]
    
    fullname = property(get_fullname, set_fullname)

    def set_participant_number(self, new_num):
        self.__participant_number = "general-", new_num
    
    def get_participant_number(self):
        return self.__participant_number


class TrialParticipant:
    
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.__chars_input = {"a": 0, "g": 0, "k": 0, "o": 0}
    
    def recordKeyPress(self, char_pressed):
        if char_pressed in self.__chars_input:
            self.__chars_input[char_pressed] += 1
        else:
            return "Charachter not in dictionary"
    
    def getkeypressinfo(self):
        return self.__chars_input
    
    def set_participant_number(self, new_num):
        self.__participant_number = "trial-", new_num
    
    def get_maxkeypress(self):
        max_keypress = []
        char_dict = self.getkeypressinfo()
        max = ("":0)
        for char in char_dict:
            max = (char)
            char_count = char_dict[char]
