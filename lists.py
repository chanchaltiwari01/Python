marks = [98, 78, 89, 68, 52]

print(marks)
print(type(marks))

print(marks[0]) #98
print(marks[2])  #89
print(len(marks))

student = ["karan" , 95.5, 17, "Delhi" ]
print (student)

student[0] = "shirish"
student[3] = "bhopal"

print(student)

#give error list index out of range .
#print (student[5])

#list  slicing 
marks = [ 86 , 78, 98, 76, 70]
print (marks[1:4]) # [78 , 98, 76] last index are ignore same as string

print (marks[-3:-1]) #[98,76]


#list methode 
list = [10 , 3, 1,4 ,5 , 7 ,8] 
list.append(9)
print (list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

list.reverse()
print(list)
list.insert(3, 9)
print(list)

char=["x-ray", "yellow", "dog" , "cat" , "boy" , "apple"]
char.sort()
print(char)

list.remove(9)
print(list)

list.pop(3)
print(list)