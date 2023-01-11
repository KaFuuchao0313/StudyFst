n=int(input())
s=[]
while n>0:
    s.insert(0,n%2)
    n=n//2
for i in range(len(s)):
    print(s[i],end=' ')