# ⭐ Day 12 – break & continue

# 🔹 break → loop थांबवते

# print until 4 when i becomes 5 it breaks the for loop

for i in range(10):
    if(i == 5):
        break
    print(f"i = {i}")  # 0 1 2 3 4

# 🔹 continue → current iteration skip

# here value of 3 gets skipped itsnot printed
for i in range(10):
    if i == 3:
        continue
    print(i)  # 0 1 2 4 5 6 7 8 9