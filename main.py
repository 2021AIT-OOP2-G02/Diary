from diaries.DiarySample import DiarySample
from diaries.koikeDiary import koikeDiary

diaries = [DiarySample(), 
            koikeDiary(),
        ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()