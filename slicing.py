#String slicing is specificing char of a string with a start index - end index (Not including the number)
#Slicing = [First number:Last number]
myname = 'Bob Smitten'
dude = ' is a dude'
print(len(myname)) #Output: 11
print(myname[0]) #Starting letter of the string
print(myname[1:]) #Slice from second letter to end.
print("dude " + myname[0:]) #concatenate two strings from start
print(myname[0:3] + ' is a dude') #Concatenate myname with string at the end
print(myname[:-1]) #Slice not including the last letter
print(myname[:-3])
print(myname[0:1])
print(myname[:1]) #End index 0 displayed
print(dude[1:3] + myname[1:3]) #Output: isob

#More practice with slicing using expedition 33
exp = "expedition33"
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
print(len(exp))
print(exp[0:10])
print(exp[10:])
print(exp[0:4])
print(exp[0:3])
print(exp[0:-8])
print(exp[-11:-8]) #When using negative for slicing larger number goes first, smaller goes last
print(exp[1:11])
print(exp[0:-2])
print(exp[0:10])
print(lst[0:5])
print(lst[-10:-5])
print(lst[0:-5])
print(lst[-10:5])
print(lst[6:])
print(lst[-4:])
print(lst[-4:])
print(lst[1:])
print(lst[-9:])
print(lst[0:9])
print(lst[-10:-1])

#Slicing = [Start: end : steps]
print(exp[0::2])
print(lst[0::3])
print(lst[-10::3])
print(lst[::-1])
print(exp[::-1])
print(exp[0::2])
print(exp[1::2])
print(lst[2:9])
print(lst[1:9])

t = "abcdefghijklmnopqrstuvwxyz"
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(len(t))
print(t[-5:])
print(t[21:])
print(t[5:21])
print(t[-21:-5])
print(t[2::4])
print(t[-24::4])
print(t[::-2])
print(nums[2:5])
print(nums[:3:-2])
print(nums[3:6])
print(nums[3:])
print(nums[::2])
print(lst[8:2:-1])
