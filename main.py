from diaries.DiarySample import DiarySmaple
from diaries.koikeDiary import koikeDiary

diaries = [DiarySmaple(), 
            koikeDiary(),
        ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()