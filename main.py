from diaries.DiarySample import DiarySmaple

diaries = [DiarySmaple(), ]

for d in diaries:
    print("----")
    print(d.get_data())
    print(d.get_summary())
    print(d.get_author())
    print()