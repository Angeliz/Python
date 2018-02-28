#从2到i-1测试是否可以整除
"""
def is_prime_number(i):
	is_prime= True
	if i==1:
		is_prime= False
	elif i!=1 and i!=2:
		for j in range(2,i):
			if i%j==0:
				is_prime= False
	if is_prime==True:
		return True
	else:
		return False

i=input("Enter a number:")
i=int(i)
print(is_prime_number(i))
"""

#去掉偶数后，从3到i-1，每次+2
"""
def is_prime_number(i):
	is_prime= True
	if i==1 or i%2==0 and i!=2:
		is_prime= False
	else:
		for j in range(3,i,2):
			if i%j==0: 
				is_prime= False
	if is_prime==True:
		return True
	else:
		return False

i=input("Enter a number:")
i=int(i)
print(is_prime_number(i))
"""

#无需到x-1，到sqrt（x）就够了
import math
def is_prime_number(i):
	is_prime= True
	if i==1 or i%2==0 and i!=2:
		is_prime= False
	else:
		for j in range(3,int(math.sqrt(i)+1),2):
			if i%j==0: 
				is_prime= False
	if is_prime==True:
		return True
	else:
		return False

i=input("Enter a number:")
i=int(i)
print(is_prime_number(i))

print("hello world!")