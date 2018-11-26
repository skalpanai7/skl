n,m=map(int,raw_input().split())
l1=[int(x) for x in raw_input().split()]
l2=[int(x) for x in raw_input().split()]
count=0
if(len(l1)==n and len(l2)==m ):
	for i in l2:
		if i in l1:
			count= count+1
	if(count==len(l2)):
		print "YES"
	else:
		print "NO"
