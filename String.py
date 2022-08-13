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
print(name[0:]) 

#step operator ::
print(name[0::4]) 
print(name[0:8:4]) 

#slicing unknow input
a=input("Enter u r name\n")
val=len(a)   #assign the length of str in val
print(a[0:val-1]) 
print(a[-val:val])

#string reverse
print('reverse=',a[::-1]) 
print(a[6:0:-2]) 
print('step operator=',a[::3]) 

#palindrome 
p='malayalam'
r=p[::-1]
print(p,r,sep='\n')
print('palindrome=',p==r)

#string multiples
A=input()
print(A*2)