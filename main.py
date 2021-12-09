from diaries.DiarySample import DiarySmaple
from diaries.OnogiDiary import OnogiDiary

diaries = [
    DiarySmaple(),
    OnogiDiary(),
 ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()