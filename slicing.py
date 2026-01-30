#String slicing is specificing char of a string with a start index - end index (Not including the number)
myname = 'Bob Smitten'
dude = ' is a dude'
print(len(myname))
print(myname[0]) #Starting letter of the string
print(myname[1:]) #Slice from second letter to end.
print("dude " + myname[0:]) #concatenate two strings from start
print(myname[0:3] + ' is a dude') #Concatenate myname with string at the end
print(myname[:-1]) #Slice not including the last letter
print(myname[:-3])
print(myname[0:1])
print(myname[:1]) #End index 0 displayed
print(dude[1:3] + myname[1:3])