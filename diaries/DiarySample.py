from diaries.AbstractDiary import AbstractDiary

class DiarySmaple(AbstractDiary):
    def get_data(self):
        return "2021-12-01"
    
    def get_summary(self):
        return ":何もない一日だった"
    
    def get_author(self):
        return "Sample"
