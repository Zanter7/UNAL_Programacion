#def f(C, K, T, I):
#  for i in range(T):
#    K = K*(1+I)-C
#  return K


def f(x):  
  return 3*x*x-2*x-3
 
def biseccion(a, b): #, K, T, I):
  epsilon = 0.0000001
  print(a,b)
  m = (a+b)/2
  if(abs(b-a)<=epsilon): return m
  if(abs(f(a))<=epsilon):
    return a
  if(abs(f(b))<=epsilon):
    return b
  if((f(a)>0)!=(f(m)>0)):
    return biseccion(a,m)
  return biseccion(m,b)

#K = float(input('Capital:'))
#I = float(input('Interes mensual %:')) / 100
#T = int(input('Duración Meses:'))
r = biseccion(0,4)
print('Raiz:',r)