class Thesaurus:

    def __init__(self, words):
        self.__words = words
        self.word_keys = list(self.__words.keys())  # [0, 1, 2]
        self.word_counter = 0
        self.synonym_counter = 0
        self.current_word = self.word_keys[self.word_counter]
        print(self.word_keys)

    def show_word(self):
        self.current_word = self.word_keys[self.word_counter]
        print("current word:",  self.current_word)
        print("show_word() has been called!")

    def show_synonym(self):
        list_of_synonyms = self.__words[self.current_word]
        current_synonym = list_of_synonyms[self.synonym_counter]
        print("current synonym:", current_synonym)
        print("show_synonym() has been called!")

    def next_word(self):
        # boolean variable to control what value is being returned: True or False
        out_of_words = False
        word_amount = len(self.word_keys)
        last_word = word_amount - 1
        self.word_counter = self.word_counter + 1
        if self.word_counter > last_word:
            self.word_counter = last_word
            print("out of range")
            out_of_words = True
        else:
            out_of_words = False
        return out_of_words

"""
# ----------
study_words = {
    "investigate": ["explore", "examine", "inspect", "interrogate", "study", "examine"],
    "reveal": ["announce", "affirm", "declare", "explain", "report", "inform"],
    "idea": ["belief", "concept", "suggestion", "thought", "plan", "pitch"]
}

thesaurus_1 = Thesaurus(study_words)
thesaurus_1.show_synonym()


#user_in = input("select option: ")
#out_of_words = False
# while user_in != "q" and out_of_words == False:
#  user_in = input("select option: ")
#  thesaurus_1.show_word()
#  out_of_words = thesaurus_1.next_word()
#  print("=============")
# print("goodbye!")
"""