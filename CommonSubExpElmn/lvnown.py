n = int(input("Enter no. of exprs: "))
exprs = []

for i in range(n):
    exprs.append(input(f"Enter expr ${i+1}: "))

print(exprs)

ht = {}

res = []

for expr in exprs:
    if expr[0] in ht.values():
        ht = {key:val for key, val in ht.items() if val != expr[0]}
    if expr[2:] in ht.keys():
        res.append(expr.replace(expr[2:], ht[expr[2:]]))
        ht[expr[2:]] = expr[0]
    else:
        ht[expr[2:]] = expr[0]
        res.append(expr)

print(res)
