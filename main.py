from diaries.DiarySample import DiarySample
from diaries.SoraDiary import SoraDiary
from diaries.WadaDiary import WadaDiary
from diaries.suzuki_Diary import suzuki_Diary
from diaries.NagisaDiary import NagisaDiary
from diaries.OnogiDiary import OnogiDiary
from diaries.koikeDiary import koikeDiary
from diaries.TakanoDiary import TakanoDiary

diaries = [
    DiarySample(),
    WadaDiary(),
    suzuki_Diary(),
    SoraDiary(),
    NagisaDiary(),
    OnogiDiary(),
    koikeDiary(),
    TakanoDiary()
 ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()