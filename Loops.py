#Loops - Hackerrank Problem 


i = int(input())
j=0


if i>=1 and i<=20:
    for j in range(i):
        print(j*j)
        i+=1
    
else:
    print('Broke Constraint!!! --> i<=0 or i<20 ')
