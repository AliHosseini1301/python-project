#پیدا کردن ریشه های x*3-x*2+2
def func( x ):
    return x * x * x - x * x + 2
 
def derivFunc( x ):
    return 3 * x * x - 2 * x
 
def newtonRaphson( x ):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
         
        x = x - h
     
    print("The value of the root is : ","%.4f"% x)
 
x0 = -20 
newtonRaphson(x0)

#اعدادارمسترانگ
'''for n in range(10,10000): 
 sum=0
 my_str=str(n)
 k=len(my_str)
 for i in range(0,k):
   sum=sum+pow(int(my_str[i]),k)

 if(sum==n):
   print("This is an Armstrong number : ", n)'''
   
#رمزنگاری به روش ژولیوسزار
'''def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
text = "ATTACKATONCE"
s = 4
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))'''

#مقسوم علیه
'''n=int(input("enter number:"))
k= int(input("enter numer:"))
for i in range(1,n):
    if(n%i==0):
        if(k%i==0):
            print(i)'''
#محاسبه sinx
n=int(input("enter limit:"))
x=int(input("enter degrees:"))
x=x*3.14/180
print(x)
p=1
f=1
s=x
sine=-1
for i in range(3,n+1,2):
    x=x*sine
    p=pow(x,i)
    f=f*i*(i-1)
    s=s+p/f
print(s)#sinx

