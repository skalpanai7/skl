num=int(raw_input())
list=[int(x) for x in raw_input().split()]
for i in range(0,num):
	for j in range(i+1,num):
		for k in range(j+1,num):
			if list[i]+list[j]==list[k]:
				print list[i],list[j],list[k]
