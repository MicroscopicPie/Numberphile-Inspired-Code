import numpy as np
import matplotlib.pyplot as plt

print("Input a value for n:\n")
n=int(input(""))
n1=n
n2=n

x=np.zeros(n**2)
y=np.zeros(n**2)
z=np.zeros(n**2)
oldz=np.zeros(n**2)
new_x=np.zeros(2016)
new_y=np.zeros(2016)

ordered_x=np.zeros(n**2)
ordered_y=np.zeros(n**2)

numberspiral=np.zeros([n1,n2])
knight_jumps=np.zeros(2016)
knight_jumps[0]=1

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

numloop=0

for i in range (0,n2):
    for i2 in range (0,n2):
        
        z[numloop]=numberspiral[i,i2]
        oldz[numloop]=numberspiral[i,i2]
        x[numloop]=i
        y[numloop]=i2
        numloop=numloop+1
        
    #end loop
#end loop

a=np.argmin(oldz)
new_x[0]=x[a]
new_y[0]=y[a]

for i in range (0, 2015):
  
#calculating all possible knight moves, for each coordinate

#for x

    big_positive_x=int(x[a]+2)
    big_negative_x=int(x[a]-2)
    small_positive_x=int(x[a]+1)
    small_negative_x=int(x[a]-1)

#for y

    big_positive_y=int(y[a]+2)
    big_negative_y=int(y[a]-2)
    small_positive_y=int(y[a]+1)
    small_negative_y=int(y[a]-1)

#combine these in the numberspiral 
#to find the possible positions for the knight to move to

    knight1=numberspiral[big_positive_x,small_positive_y]
    knight2=numberspiral[big_positive_x,small_negative_y]
    knight3=numberspiral[big_negative_x,small_positive_y]
    knight4=numberspiral[big_negative_x, small_negative_y]
    knight5=numberspiral[small_positive_x, big_positive_y]
    knight6=numberspiral[ small_negative_x,big_positive_y]
    knight7=numberspiral[small_positive_x, big_negative_y ]
    knight8=numberspiral[small_negative_x, big_negative_y]
    
    possible_choices=np.array([knight1, knight2, knight3, knight4, knight5, knight6, knight7, knight8])
    
    for i2 in range (0,i):
        for i3 in range (0,8):
            if knight_jumps[i2]==possible_choices[i3]:
                possible_choices[i3]=(n2**2)+1
            
            #end if
        #end for
    #end for
     


    smallest_square=min(possible_choices)
    knight_jumps[i+1]=int(smallest_square)
    
    for i7 in range (0,(n2**2)):
        if smallest_square==oldz[i7]:
            a=i7
        #end if
    #end loop
    new_x[i+1]=x[a]
    new_y[i+1]=y[a]
#end loop   

for i in range (0,n2**2):
    a=np.argmin(z)
    ordered_x[i]=-x[a]
    ordered_y[i]=y[a]
    z[a]=(n2**2)+1
#end loop
 
  
"""
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=np.inf)
"""
new_y=new_y*1
new_x=new_x*-1
    
plt.plot(ordered_y, ordered_x, color='gold') #comment this line out to remove gold square
plt.plot(new_y, new_x, linestyle='none',marker='.',markersize='1', color='black') #comment this line out to remove black dots (where knight lands)
plt.plot(new_y, new_x, linestyle='-', color='royalblue', linewidth='1') #this plots the movement of the knight
plt.plot(44,-12, marker='x', color='red', markersize='3') #this plots where the knight ends
plt.plot(34,-35, marker='o', color='magenta', markersize='3', fillstyle='none') #this plots where the knight starts
plt.axis('off')
plt.axis('square')

plt.savefig('The Trapped Knight with Overlay.tiff', format='tiff', dpi=2000)





