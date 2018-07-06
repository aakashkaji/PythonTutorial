### python generators example here

def generator_exp():
	for i in range(1,10):
		yield i
x=generator_exp()
for a in x:
	print(a)

#python generators are used in calculate large set of resource becoz they don't store any value	
def fibon(n):
	a=b=1
	print('calling')
	for i in range(n):
		yield a
		a,b=b,a+b
for x in fibon(10):
	print(x)

#class using generator very very important
#generator helps in work when data is in millions becoz it takes less memory space it doesn't store data in memory it stores on fly
# Generator returns iterator ..and it iterates once 

class Aakash:
	value=0
	def __init__(self,value):
		self.value=value
	#instance  method	
	def generator_fibo(self):
		a=b=1
		for i in range(self.value):
			yield a
			a,b=b,a+b
	@classmethod
	def fact(cls):
		sum=1
		for i in range(1,cls.value+1):
			sum=sum*i
		return sum
	@staticmethod
	def fact_static(v):
		sum=1
		for i in range(1,v+1):
			sum=sum*i
		return sum	


obj1=Aakash(10)
fun=obj1.generator_fibo()
print([i for i in fun])
		
Aakash.value=5
print(Aakash.fact())
#print(dir(obj1))
#print(dir(Aakash))
print(Aakash.fact_static(6))
