n=int(raw_input())
l=[int(x) for x in raw_input().split()]
r=[]
for i in range(0,n):
	for j in range(i+1,n):
		if l[i]==l[j]:
			r.append(l[j])
print r[0]
