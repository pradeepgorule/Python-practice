# 📌 1️⃣ Strings in Python

# 🔹 Important String Methods
# Method                What it does
#-------------------------------------------------

# lower()               Convert to lowercase
# upper()               Convert to uppercase
# strip()               Remove spaces
# replace()             Replace text
# split()               Convert string to list
# find()                Find index

text = 'Hello Python ....'

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace('Python','Javascript'))
print(text.split())


# 📌 2️⃣ String Slicing

# Slicing syntax:

# string[start:end:step]

slicingText = "pradeep"

print(slicingText[0:3]) # pra
print(slicingText[:4])  # prad
print(slicingText[2:])  # adeep
print(slicingText[:: -1]) # peedarp 
