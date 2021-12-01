from filemanager import *
from thesaurus import Thesaurus

thesaurus_filemanager = ThesaurusFileManager("thesaurusfilemanager.txt")


study_words = {
    "investigate": ["explore", "examine", "inspect", "interrogate", "study", "examine"],
    "reveal": ["announce", "affirm", "declare", "explain", "report", "inform"],
    "idea": ["belief", "concept", "suggestion", "thought", "plan", "pitch"]
}

synonym1 = thesaurus_filemanager.get_line_number_dict(7)
thesaurus_1 = Thesaurus(synonym1)
print(thesaurus_1.show_synonym())