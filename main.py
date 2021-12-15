from diaries.DiarySample import DiarySample
from diaries.suzuki_Diary import suzuki_Diary

diaries = [
    suzuki_Diary()
 ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()