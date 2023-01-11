td=[34,31,29,36,28,25,26,27,32,35,32]
n=len(td)
total=0
c=0

for i in td:
    total=total+i

aver=round(total/n,2)

for j in td:
    if j<aver:
        c=c+1

print(aver)
print(c)