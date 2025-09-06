tup = (1 , 2 , 3)
print (type(tup))
print(tup[0])

# dont allow assignment.
#tup[0]=0;

tup1 = ()
print(type(tup), tup1)

tup1 =(1,)
tup= (2)
print(type(tup1), tup1)
print(tup) 
print(type(tup))

tup = (1 , 2, 3, 4, 2, 5, 2, 7, 8, 9)
print (tup.count(2))
print(tup.index(2))