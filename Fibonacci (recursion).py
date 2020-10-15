#Recursive Fibonnaci Method

from timeit import default_timer as timer
# time
start = timer()

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    

for i in range(35):
    print(fib(i))

# measure elapsed time
end = timer() #timing
print("elapsed time (s):" ,end - start)

