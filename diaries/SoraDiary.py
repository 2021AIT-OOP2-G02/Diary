from diaries.AbstractDiary import AbstractDiary

class SoraDiary(AbstractDiary):
    def get_data(self):
        return "2021-12-09"
    
    def get_summary(self):
        return ":何もない一日だった"
    
    def get_author(self):
        return "Sora"
