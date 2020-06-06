wh =  4
wl = 4

for x in range(1,wh+1):
    for y in range(1,wl+1):
        if x!=wh:
            print(" ",end='')
        else:
            print('*',end='')
        for z in range(1,5):
            if x==1 or z==1 or z==4:
                print('*',end='')
            else:
                print(" ",end='')
        if x!=wh:
            print("  ",end='')
        else:
            print('*',end='')
    print()


"""
# p[attern 

 ****   ****   ****   ****
 *  *   *  *   *  *   *  *
 *  *   *  *   *  *   *  *
**  ****  ****  ****  **

"""