# Slicing in String
# 1. Normal 
# 2. Pattern

# 1. Normal Slicing

# Syntax : variableName[starting index value:Range]
# Slicing start from zero(0), Negative Slicing start from backward and -1
 
#Example
x="Hello_Everyone@2346"
# print one
print(x[11:14])
# print Ever
print(x[6:10])

#Negative Indexing

x="Hello_one@2346"
# print @23
print(x[-5:-2])
# print ello
print(x[-13:-9])


# 2. Pattern Slcing

# Syntax: variablename[starting index value:Range:step]
# both Negative and positive indexing are possible
# by defalut starting index=0, step=1, Range= last character

x="Hello_Everyone@2346"
# print Eey
print(x[6:11:2])
#print ovye
print(x[4:14:3])

# Negative Indexing

#print yn@
print(x[-9:-4:2])

# Backward side slicing

#print eno
print(x[-6:-9:-1])
#print nyeE
print(x[-7:-14:-2])
#print nrE
print(x[12:5:-3])





