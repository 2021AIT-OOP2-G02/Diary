from diaries.DiarySample import DiarySample
from diaries.OnogiDiary import OnogiDiary

diaries = [
    DiarySample(),
    OnogiDiary(),
 ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()