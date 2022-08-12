#DATATYPES OF PYTHON 
#1.int 2.float 3.complex 4.bool 5.str 

#1.int data type  
n=10
n1=20
#binary conversion
bn=0b011
an=0b111
print(bn,an)
#octal conversion
o1=0o767
o2=0o345
print(o1,o2) 
#hexadecimal
x1=0xf7
x2=0xa3
print(x1,x2) 

#using built-in func 
#bin() func
no=bin(20)
print(no) 
#oct() func
no=oct(20)
print(no) 
#hex() func
no=hex(20)
print(no)  

#2.float dta type
no=2.3456789
print(no)
print(type(no))
no=9.9e3
print(no)  

#3.Complex data type
no1=3+9j
print(type(no1))
no2=4+5j 
tot=no1+no2
print(tot) 
print(tot.real)
print(tot.imag)  

#4.Boolean data type
print(n<n1,n>n1,n==n1,n!=n1,sep='\n') 
present=True
print(present)
print(type(present))
print(True+True,True+False,False+False,sep='\n') 

#5.STRING data type
Name='saiharish'
#usage of triple quotes
statement='''he say's"hi"thamizh how are you'''
#Paragraph
Address='''41-pidari east street     
sirkali-609110''' 
print(Name,statement,Address,sep='\n') 

# 5.1.String slicing  
  #1.a Forward slicing -+ve strts from 0 
print(Name[0])
print(Name[1])
print(Name[2])
  #1.b Backward slicing --ve strts from -1 
  #s  a  i
  #-3 -2 -1
print(Name[-1])
print(Name[-2])
print(Name[-3])

# 2.slicing whatever we want using ':'
name='rajarajachozhan'
print(name[0:8])
print(name[8:]) 
print(Name[0:3])
print(Name[3:]) 
print(Name[:3])