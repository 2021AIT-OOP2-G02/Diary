from diaries.AbstractDiary import AbstractDiary

class NagataniDiary(AbstractDiary):

    def get_data(self):
        return "2021-12-09"

    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習２"""

    def get_author(self):
        return "Onogi"