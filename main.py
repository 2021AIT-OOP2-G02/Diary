from diaries.DiarySample import DiarySmaple
from diaries.NagisaDiary import NagisaDiary

diaries = [DiarySmaple(), 
           NagisaDiary(),
]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()