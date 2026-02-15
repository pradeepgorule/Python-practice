# 1️⃣ Reverse a string (without using [::-1])

text = "developer"
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)

# 2️⃣ Count how many times a character appears

countString = "mississippi"
character = 's'
count = 0
for char in countString:
    if(char == 's'):
        count+=1
        continue
print(f'count is {count}')

# 3️⃣ Remove all spaces from a string

spaceText = "Hello Python World"
print(spaceText.strip())


# 5️⃣ Check if a string is palindrome

cartext = "racecar"
palindromeText = cartext[::-1]

if(cartext == palindromeText):
    print('palindrome')
else : print('not a palindrome')

# 6️⃣ Remove duplicates from list (keep order same)

array = [1, 2, 2, 3, 4, 1, 5]
finalArr = []
for num in array:
    if(array.count(num) >= 1 and num not in finalArr):
        finalArr.append(num)

print(finalArr)