# ✅ 1️⃣ Reverse a String

# Method 1 (Best Way)
text = "Pradeep"
print(text[::-1])

# Method 2 (Using loop)
reversed_text = ""
for char in text:
    print(char)
    reversed_text= char + reversed_text
print(reversed_text)


# ✅ 2️⃣ Find Duplicates in List

numbers = [1, 2, 3, 2, 4, 1, 5]

duplicates =[]

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print(f'duplicates {duplicates}')