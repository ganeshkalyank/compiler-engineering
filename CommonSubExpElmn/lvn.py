n=int(input("Enter no.of expression : "))
expr=[]
ip=[]
for i in range(n):
	c=input("Enter the postfix expression of 5(3 operand and 2 operations) : ")
	ip.append(c)
	if(ip[i][4] != '=')or (len(ip[i]) != 5) or (ip[i][3] not in['+','-','*','/']):
		print("Enter a valid Input.")
		i=i-1
		continue
	expr.append(c)
k=0
l=[]
print("The Common sub expression elimination : ")
for i in range(n):
	c=expr[i][1:4]
	for j in range(i+1,n):
		if c==expr[j][1:4] and c!= "temp":
			x=expr[j]
			t=x[1:4]
			if k!=0:
			    v=0
			    for a in l:
			        if c==expr[j][1:4]:
			            t1=x[1:6]
			            y=x.replace(t1,'temp'+str(v))
			            expr[j]=y
			            v=v+1
			else:
			    y=x.replace(t,'temp'+str(k))
			    expr[j]=y
			    l.append("temp"+str(k)+"="+t)
			    k=k+1
print(expr)
print(l)
