#find unique element
s1 = {1, 2, 3, 5, 3}
s2 = {3, 5, 7}
s3 = s1.symmetric_difference(s2)
print(s3)

#remove duplicate

s5 = s1 | s2
print(s5)

#perform set operation 

s4 = s1.intersection(s2)
s6 = s1.union(s2)
s7 = s1.difference(s2)

print(s4)
print(s6)
print(s7)

#check element exit in set

x = 5
if x in s6:
    print("True")

#verify subset

print(s7.issubset(s6))

