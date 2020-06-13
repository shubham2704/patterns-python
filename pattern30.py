n = 5

for x in range(n//2,n+1,+2):
    for y in range(1,n-x,+2):
        print(' ',end='')
    for y in range(1,x+1):
        print('*',end='')
    for y in range(1,n-x+1):
        print(' ',end='')
    for y in range(1,x+1):
        print('*',end='')
    print()

for x in range(n,0,-1):
    for y in range(x,n):
        print(' ',end='')
    for y in range(1,(x*2)):
        print('*',end='')
    print()


"""
# pattern 

 **   **
**** ****
*********
 *******
  *****
   ***
    *

"""