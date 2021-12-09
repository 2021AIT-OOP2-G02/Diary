from diaries.AbstractDiary import AbstractDiary

class DiarySmaple(AbstractDiary):
    def get_data(self):
        return "2021-12-09"
    
    def get_summary(self):
        return ":ねむい！！"
    
    def get_author(self):
        return "wadatakeru"
