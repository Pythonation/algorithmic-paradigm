# Dynamic Programming Fibonnaci Method
from timeit import default_timer as timer
start = timer()

F = [-1]*500 #array to store fibonacci terms

def dynamic_fibonacci(n):
  if (F[n] < 0):
    if (n==0):
      F[n] = 0
    elif (n == 1):
      F[n] = 1
    else:
      F[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
  return F[n]

for i in range(35):
    print(dynamic_fibonacci(i))

end = timer()
print("elapsed time (s):" ,end - start)

