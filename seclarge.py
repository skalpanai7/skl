n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
l.sort()
m=l[::-1]
print(m[k-1])
