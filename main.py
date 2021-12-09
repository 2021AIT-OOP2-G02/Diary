from diaries.DiarySample import DiarySmaple
from diaries.k20066Diary import DiarySmple

diaries = [DiarySmaple(), ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()