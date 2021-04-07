import math
## matrix size is wxh  with three times given
w, h, t1, t2, t3 = [int(i) for i in input().split()]
a,a2,o = [],[],{}
a3 = [["." for i in range(w)] for j in range(h)]
for i in range(h):
    fr, sr = input().split()
    a.append(fr)
    a2.append(sr)
for x in range(len(a)):
    for y in range(len(a[0])):
        #if a[x][y] == "A": print(x,y)
        if a[x][y] != ".":
            o[a[x][y]] = [x,y]
#print(o)
#print(a)
#print(a2)
#print(w,h)
#print(t1,t2,t3)
newx=0
newy=0
timediff=0
for x in range(len(a)):
    for y in range(len(a[0])):
        #if a2[x][y] == "A": print(x,y)       
        if a2[x][y] != ".":
            tup = o[a2[x][y]]
#           print(tup,x,y,)
            num = tup[0]
            den = tup[1]
            delx = (x-tup[0])/(t2-t1)
            dely = (y-tup[1])/(t2-t1)
            #m=math.floor((y-tup[1])/x-tup[0])
            #print(delx,dely)
            if t3<t2:
                newx = math.floor(t2 - delx * (t2-t3))
                newy = math.floor(t2 - dely * (t2-t3))
                if t3 < t1:
                    newx = math.floor(tup[0] - delx * (t1-t3))
                    newy = math.floor(tup[1] - dely * (t1-t3))
            else:
                #print(y,dely)
                newx = math.floor(x + delx * (t3-t2))
                newy = math.floor(y + dely * (t3-t2))

            if newx < 0 or newx >= w or newy < 0 or newy >= h:
                continue
            #print(newx,newy)
            if a3[newx][newy] != ".":
                if ord(a3[newx][newy]) > ord(a2[x][y]):
                    a3[newx][newy] = a2[x][y]
            else:
                a3[newx][newy] = a2[x][y]
for x in range(len(a)):
    print("".join(a3[x]))
