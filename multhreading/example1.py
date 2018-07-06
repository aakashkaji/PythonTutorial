import time
import threading

def square_of_number(val):
	print("calculate square of numbers:")
	for n in val:
		time.sleep(0.2)
		print("square=",n*n)

def cube_of_number(val):
	print("cube of number:")
	for n in val:
		time.sleep(0.2)
		print("cube=",n*n*n)

ls=[2,3,4,5]

t=time.time()
th1=threading.Thread(target=square_of_number,args=(ls,))
th2=threading.Thread(target=cube_of_number,args=(ls,))
#square_of_number(ls)
#cube_of_number(ls)
th1.start()
th2.start()
th1.join()
th2.join()
print("time done in: ",time.time()-t)
