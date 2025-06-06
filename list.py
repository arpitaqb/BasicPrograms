#find the greatest string in list.
a = ["aaaa", "aaa", "aaaaaa"]

def fun1(string):
    return max(string, key=len)

l = fun1(a)
print(l)


#print number which is greater then 5
a = [ 2, 5, 7 , 9, 3, 8]

for x in a:
    if x >= 5:
        print(x)
    

#find duplicate 
"""
def fun1(a):
    a1 = set()
    a2 = set()
    for item in a:
        if item in a1:
            a2.add(item)
        else:
            a1.add(item)
    return list(a2)

a = [1, 3, 6, 3, 8, 1, 5]
b = fun1(a)

print(b)
"""

#reverse string 
"""
a = [1, 2, 3, 4, 5] 
a.reverse()
print(a)
"""

#sum of elements
a  = [1, 2, 3, 4, 5]
total = 0
for x in a:
   total += x

print(total)    
