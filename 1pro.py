data = {2020: 5, 2021: 4, 2022: 6, 2023: 2}
max_stars = max(data.values())
for i in range(max_stars, 0, -1):
    for year in sorted(data):
        if data[year] >= i:
            print("*", end="\t")
        else:
            print(" ", end="\t")
    print()