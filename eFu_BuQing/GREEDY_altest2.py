c=input()
txt=c.split(" ",-1)
for i in text:
    i=int(i)
n=int(input('n='))
grl=[0]
if n==0:
    print(0)
else:
    for i in range(1,n+1):
        if i<2:
            grl.append(grl[i-1]+1)
        elif i<5:
            grl.append(min(grl[i-1]+1,grl[i-2]+1))
        else:
            grl.append(min(grl[i-1]+1,grl[i-2]+1,grl[i-5]+1))
    print(grl[n])   