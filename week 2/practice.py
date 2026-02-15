# Check if a character is a vowel or consonant

vowelCharacters = ['a','i','e','o','u']

char = input("Enter your character ")

if char in vowelCharacters:
    print('its vowel')
else : print('not a vowel')

# Password validation

password = input("Enter your password ")

if '@' in password:
    print('valid')

else : print('invalid')


# Print numbers from 1 to 50 s

for i in range(1,51):
    print(i)

# Print only even numbers from 1 to 30 (continue वापरून)

for i in range(1,31):
        if( i % 2 != 0):
            continue
        print(i)


# Find the sum of first 10 natural numbers (while loop)

natNum = 0
finalValue = 0

while natNum <= 10:
    print(natNum)
    finalValue = finalValue + natNum
    natNum+= 1
    
print(finalValue)

# 🔶 7. Stop loop when number becomes 7 (break वापरून)

for i in range(10):
    if(i == 7):
        break
    print(i)

# 🔶 9. Count vowels in a string

name = input('Enter your name')
vowelCount = 0
for i in name:
    if(i in vowelCharacters):
        vowelCount+=1

print(vowelCount)