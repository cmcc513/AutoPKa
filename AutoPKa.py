from math import log
from time import time
from decimal import Decimal
from random import choice

def multiply(l,b):
	m = 1
	for i in range(0,b):
		m *= l[i]
	return m
st = -20
print("AutoPka. For those who find acid-base chemistry boring. Author: David Huang")
print()
Ka = []
c = []
z = int(input("How many kinds of acid/base:"))
for i in range(z):
	print("Acid/Base",str(i+1)+":","Please insert pKa/pKb(s) in the following line.")
	Ka.append([Decimal(10**(-eval(x))) for x in input().split()])
	c.append(Decimal(eval(input("Insert concentration:"))))
dep = Decimal(eval(input("Concentration of added base/acid:")))
Hplus,Hplus0 = [10**(-Decimal(x)) for x in input("Enter 2 estimated pH/pOH values:").split()]

x,y = Hplus,Hplus0

print()
print("Processing...")
print()
t1 =time()

'''
up = [m*(Hplus**(n-m))*multiply(Ka,m) for m in range(n,0,-1)]
down = [multiply(Ka,m)*(Hplus**(n-m)) for m in range(n,0,-1)]+[Hplus**n]
right = (10**(-14)/Hplus+(sum(up)/sum(down))*c)
'''
def g(Hplus,Ka,i):
	n = len(Ka)
	up = [m*(Hplus**(n-m))*multiply(Ka,m) for m in range(n,0,-1)]
	down = [multiply(Ka,m)*(Hplus**(n-m)) for m in range(n,0,-1)]+[Hplus**n]
	right = ((sum(up)/sum(down))*c[i])
	return right
	
def f(Hplus):
	s = sum(g(Hplus,Ka[i],i) for i in range(z)) - Hplus - dep + Decimal(10**(-14))/Hplus
	return s
	
k = 0
ans = []
print("First Iteration...")

while abs(f(Hplus)/Hplus) >= 1e-13:
	Hplus,Hplus0,k=Hplus-(Hplus-Hplus0)/(f(Hplus)-f(Hplus0))*f(Hplus),Hplus,k+1 #Secant Method
	print(Hplus)
print("Converged.")
ans.append(Hplus)

Hplus0,Hplus = x,y
print()
print("Second Iteration...")

while abs(f(Hplus)/Hplus) >= 1e-13:
	Hplus,Hplus0,k=Hplus-(Hplus-Hplus0)/(f(Hplus)-f(Hplus0))*f(Hplus),Hplus,k+1 #Secant Method
	print(Hplus)
print("Converged.")
ans.append(Hplus)


t2 = time()

print()
print("Finished.")
try:
	print("pH/pOH value is", "{:.5f}".format(-log(max(ans),10)))
except:
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	print("Severe Error #2070. Please change initial values.")
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print()
print(choice(["I like your tricycle.","Road cones protect my head.","I have a screen door shield.","I used to play football.","There's butter on my head.","Haaaa! Haaaaaaaaaaaa! I'm gonna eat your brains!","We are the undead!","There's a zombie in your lawn."]).upper())
print("Iteration time(s) is",k,".")
print("CPU time is",int((t2-t1)*1000),"milisecond(s).")
