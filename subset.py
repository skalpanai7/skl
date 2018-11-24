n=int(raw_input())
l=[int(x) for x in raw_input().split()]
r=[]
for i in range(0,n):
	if i%2==1:
		if l[i]%2==0:
			r.append(l[i])
	else:
		if l[i]%2==1:
			r.append(l[i])
print " ".join(map(str,r))
