# 📌 3️⃣ Lists in Python

# A list stores multiple values.

number = [10,20,30,40,50,60,70,80,90,100]

# 🔹 Important List Methods
# Method	            What it does
#-------------------------------------------
# append()              Add item
# remove()              Remove item  (it removes only first occurence check example below )
# pop()                 Remove by index
# sort()                Sort list
# reverse()             Reverse list
# count()               Count occurrences   ( get tge count of specified num in the list)


nums = [5, 3, 8, 9]

nums.append(6)
nums.remove(3)
nums.sort()
print(nums)


# remove() example

removeNum = [5,4,9,4]

removeNum.remove(4)
print(removeNum)  # [5,9,4]


# count()   example

countNum = [1, 2, 3, 2, 4, 1, 5]
print(countNum.count(1))   # 2



# 📌 4️⃣ Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6

# explantion of Nested list
# Python uses 0-based indexing. so indexing looks like 
matrix = [
    [1, 2, 3],          # index 0
    [4, 5, 6],          # index 1
    [7, 8, 9]           # index 2
]

#              col0    col1    col2
#    # row 0     1       2       3

#    # row 1     4       5       6    

#    # row 2     7       8       9



#  check the above structure 
#   matrix[1]         //   [4,5,6]
#   matrix[1][2]      //  6
# 
