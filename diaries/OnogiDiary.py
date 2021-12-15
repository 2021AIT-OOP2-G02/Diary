from diaries.AbstractDiary import AbstractDiary

class OnogiDiary(AbstractDiary):
    def get_data(self):
        return "2021-12-09"
    
    def get_summary(self):
        return ":ちょっといい日だった"
    
    def get_author(self):
        return "Onogi"
