import math 

def  suma2(x,y):

    resultado=x+y

    return resultado

def lateral(x,y,z):
    resultado=2*((x*y)+(y*z)+(x*z))
    return resultado


a=17
b=3
q=math.floor(a/b)
r=a%b;
print("q=",q)
print('r=',r)
print(suma2(a,b))

print(lateral(5,8,10))
