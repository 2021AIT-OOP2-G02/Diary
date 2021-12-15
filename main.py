from diaries.DiarySample import DiarySmaple
from diaries.TakanoDiary import TakanoDiary


diaries = [DiarySmaple(),
           TakanoDiary(),
        ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()