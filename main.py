from diaries.DiarySample import DiarySmaple
from diaries.SoraDiary import SoraDiary
from diaries.WadaDiary import WadaDiary
from diaries.suzuki_Diary import suzuki_Diary
from diaries.NagisaDiary import NagisaDiary

diaries = [
    DiarySmaple(),
    WadaDiary(),
    suzuki_Diary(),
    SoraDiary(),
    NagisaDiary()
 ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()