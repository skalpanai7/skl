n=input()
l=[int(x) for x in raw_input().split()]
l.sort()
i=0;j=n-1
min=9999
while i<j:
	if min>abs(l[i]+l[j]):
		min=abs(l[i]+l[j])
		x=l[i]
		y=l[j]
	if l[i]+l[j]<0:
		i+=1
	else:
		j-=1
print x,y
