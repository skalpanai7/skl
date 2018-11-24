n=int(raw_input())
l=[int(x) for x in raw_input().split()]
min=-1
r=[]
for i in range(0,n):
	for j in range(i+1,n):
		if l[i]==l[j]:
			min=i
			r.append(l[j])
if min!=-1:
	print r[0]
else:
	print "unique"
