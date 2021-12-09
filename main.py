from diaries.DiarySample import DiarySmaple
from diaries.SoraDiary import SoraDiary

diaries = [
    DiarySmaple(),
    SoraDiary(),
 ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()