from diaries.AbstractDiary import AbstractDiary

class koikeDiary(AbstractDiary):
    def get_data(self):
        return "2021-12-09"
    
    def get_summary(self):
        return ":初めてのGitHubでなかなかに苦戦した。チームメンバーが優しそうな人でよかった。心強い。Vtuber大好き"
    
    def get_author(self):
        return "古池"
