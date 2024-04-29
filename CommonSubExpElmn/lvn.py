def optimizer(expressions):
    value_table = {}
    for i,(target,expr) in enumerate(expressions):
        if ' ' in expr:
            L,op,R = expr.split(' ')
            if(L.isdigit() and R.isdigit()):
                if(op=='+'):
                    expressions[i] = (target,int(L)+int(R))
                if(op=='-'):
                    expressions[i] = (target,int(L)-int(R))
                if(op=='*'):
                    expressions[i] = (target,int(L)*int(R))
                if(op=='/'):
                    expressions[i] = (target,int(L)/int(R))
            else:
                L_value = value_table.get(L,ord(L))
                R_value = value_table.get(R,ord(R))
                #creating hash_key
                hash_key = (op,min(L_value,R_value),max(L_value,R_value))
                #Check dictionary value
                if hash_key in value_table:
                    expressions[i] = (target,expressions[value_table[hash_key]][0])
                    value_table[hash_key] = i
                else:
                    value_table[hash_key] = i
        value_table[target]=i
    return expressions

expressions = [
    ('t1','x + y'),
    ('t2','x + y'),
    ('t3','8 + 5'),
    ('t4','x + z'),
    ('t5','6 - 3'),
    ('t5','5 * 3'),
]

ans = optimizer(expressions)

for target,expr in ans:
    print(f"{target} = {expr}")
