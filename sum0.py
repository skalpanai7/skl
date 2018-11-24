n=int(raw_input())
l=[int(x) for x in raw_input().split()]
r=[]
for i in range(0,n):
	for j in range(i+1,n):
		if l[i]+l[j]==0:
			r.append(l[i])
			r.append(l[j])
print " ".join(map(str,r))
			
