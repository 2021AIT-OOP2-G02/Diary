from diaries.AbstractDiary import AbstractDiary

class NagisaDiary(AbstractDiary):
    def get_data(self):
        return "2021-12-09"
    
    def get_summary(self):
        return ":オブジェクト指向プログラミング演習２が大変だった"
    
    def get_author(self):
        return "nagisa"
