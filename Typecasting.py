#TYPE CASTING 
#converting one data type into another data type is type casting 
#int from float
n=99.9
print(n)
n=int(n)
print(n)

#int from boolean 
print(True+False)
print(True+True)
print(False+False) 
#let's check how we got previous output through typecasting

print('value of true is:',int(True))
print('value of false is:',int(False))
 
#we can't convert string to int
#name='sai'
#print(int(name))
#in output we got "ValueError" 

#int and float frm string 
doorno='41'
print(doorno)
print(type(doorno))
print(int(doorno))
print(type(int(doorno))) 
print(float(doorno))
print(type(float(doorno)))

# float from boolean 
print(float(True))
print(float(False))

#complex from int,float,str,bool
print(complex(10))
print(complex(14.4)) 
print(complex('10'))
print(complex(True))
print(complex(False)) 
print(complex(2,3))
#get two no and convert into complex 
c1=int(input())
c2=int(input())
print(complex(c1,c2)) 

#Boolean from other data types
print('BOOLEANS')
print(bool(1))
print(bool(0))
print(bool(1.3)) #true for any non zero values
print(bool(0.3))
print(bool(2+9j))
print(bool(0+8j))
print(bool(0+0j)) #false for zero
print(bool('10'))
print(bool('abc'))
print(bool('false'))  #true for non empty strings
print(bool(''))    #False for empty string 

#string from other data types 
print(str(10))
print(str(10.3))
print(str(10+7j))
print(str(True))
#Concadination type casting is used
#eg :
# print("Ammount:"+a) //you can't concadinate str and int
#TypeError is occur
#sort this error through Type casting 

#NO TYPE CASTING IS USED Eg:1
amount=input("Enter the Amount") #//avoid type cast on input so it can take input as str and it can be concaded
print('Amount of rent='+amount) 

#WITH USE OF TYPE CASTING Eg:2 
amount=int(input("Enter the Amount"))  
print('Amount of rent='+str(amount)) 
 #//Do type cast on the input so it can take input as str and it can be concaded