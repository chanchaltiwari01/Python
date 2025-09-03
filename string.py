str1 = "this is string .\t we are creating it in python" #\n for new line and \t for tab
print(str1)
#concationation

str1 = "chanchal"
str2 = "Tiwari"
str3 =  str1 + " " +str2 
print (str3)

#len function
len1 = len(str3)
print(len1)

#indexing 
str1="chanchal"
print(str1[7]) #L
print(str1[4]) #c

#slicing 
str4 = "chanchal Tiwari"
print (str4[2:6])
print (str4[:4]) #same as str4[0:4]
print (str4[5:]) #same as len(str)
print (str4[9:len(str4)])

#negative index 
str5 = "apple"
print (str5[-5:-1])

#string function 

str = "i am working in agnisys"

print (str.endswith("sys"))
print (str.capitalize())
print(str)
str=str.capitalize()
print(str.capitalize())

str = "i am studying javascript form my owm"
print(str.replace("javascript","python"))
print(str.find("java"))
print(str.count("form"))
