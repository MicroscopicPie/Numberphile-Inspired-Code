import numpy as np
import matplotlib.pyplot as plt

print("Input a value for n:\n")
n=int(input(""))
n1=n
n2=n

numberspiral=np.zeros([n1,n2])

b=int(n/2)
c=n2**2
d=int((n-1)/2)

if n % 2!=0:
    numberspiral[d,d]=1

for a in range (0,b):
    
    for i in range (n2-n,n):
        numberspiral[n2-n,i]=c
        c=c-1
    #end loop  
      
    c=c+1
    
    for i2 in range (n2-n,n):
        numberspiral[i2,i]=c
        c=c-1
    #end loop
     
    c=c+1
       
    for i3 in range (n-1,n2-n-1,-1):
        numberspiral[i2,i3]=c
        c=c-1
    #end loop

    n=n-1; c=c+1
    
    for i4 in range (n,n2-n-1,-1):
        numberspiral[i4,i3]=c
        c=c-1
    #end loop
#end loop   

"""
for m in range (0,n2):
    for n in range (0,n2):
        f=int(numberspiral[m,n])
        x=0                              #this filters out all non-perfect numbers
        for i in range (1,f):
            if f % i==0:
                x=x+i
            #end loop
        #end loop
        if x!=f:
            numberspiral[m,n]=0
        #end loop
    #end loop
#end loop
"""
 

for m in range (0,n2):
    for n in range (0,n2):
        f=int(numberspiral[m,n])
        x=0                             #this filters out all non-prime numbers
        for i in range (2,f):
            if f % i==0:
                numberspiral[m,n]=0
                break
            #end loop
        #end loop
    #end loop
#end loop

plt.matshow(numberspiral,cmap='binary_r', vmin=0, vmax=1)
plt.axis('off')

plt.savefig('Ulams Spiral.tiff', format='tiff', dpi=2000)
