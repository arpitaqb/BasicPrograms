# unpack tuple

t1 = ("a", "b", "c")
a, b, c = t1
print(a)
print(b)
print(c)

#swap 2 number

a = 1
b = 2

a, b = b,a

print(a)
print(b)

#merge 2 tuple and remove duplicate
t1 = (1, 2)
t2 = (1, 3)

t3 = tuple(set(t1+t2))
print(t3)

#first and last element of tuple

print(t1[0])
print(t3[len(t3)-1])

# convert int to string 
  
print(type(t3[0]))

str_t3 = tuple(str(i) for i in t3)
print(type(str_t3[0]))

