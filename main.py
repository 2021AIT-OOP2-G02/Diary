from diaries.DiarySample import DiarySmaple
from diaries.WadaDiary import WadaDiary

diaries = [
    DiarySmaple(),
    WadaDiary()
 ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()