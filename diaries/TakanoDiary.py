from diaries.AbstractDiary import AbstractDiary

class TakanoDiary(AbstractDiary):
    def get_data(self):
        return "2021-12-09"
    
    def get_summary(self):
        return "頑張ります！みなさんよろしく"
    
    def get_author(self):
        return "Sample"
