wh = 4
wl = 4
pc = wh-1

for x in range(0,wh+1):
    pchar = ord('A')
    for y in range(0,(wh*wl*2)):
        if y%(wh*2)==pc or y%(wh*2)==wh+x:
            print(chr(pchar),end='')
        else:
            print(' ',end='')
        pchar+=1
        if pchar>ord('Z'):
            pchar = pchar-26
    pc-=1
    print()

"""
PATTERN - 34

   DE      LM      TU      BC
  C  F    K  N    S  V    A  D
 B    G  J    O  R    W  Z    E
A      HI      PQ      XY      F

"""