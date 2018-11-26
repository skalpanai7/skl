num=int(raw_input())
list=[int(x) for x in raw_input().split()]
min=-1
r=[]
for i in range(0,num):
	for j in range(i+1,num):
		if list[i]==list[j]:
			min=i
			r.append(list[j])
if min!=-1:
	print r[0]
else:
	print "unique"
