nums = [50, 7, 80, 5, 8]
nums[0]
nums[1:]

nums[::-1]

names = ["dude", "man", "bob" ]

stuff = [9.5, "bob", 50]

lst = [names, stuff, nums]

nums.append(70)# Append adds numbers at the end
print(nums)

nums.insert(3, 5000)
print(nums)
nums.remove(50) # Removed element number
print(nums)
nums.pop(4) #Removes index
print(nums)
nums.clear()
print(nums)

nums = [5, 10, 15, 20, 25, 30, 35, 40]
words = ["alpha", "beta", "gamma", "delta", "epsilon"]
print(len(nums))
#1.
nums.pop(0)
nums.pop(6)
nums.extend(nums[1:5])
print(nums)
#2.
nums.pop(4)
print(nums)

#3.
words.insert(0, "START")
print(words)

#4
words.remove("gamma")
print(words)
words.pop(2)
print(words)

#5.
print(nums[4:])

#6.
nums.append(nums[0:4])
print(nums)

#7
print(words[::-1])

#8
del words[2:]
print(words)