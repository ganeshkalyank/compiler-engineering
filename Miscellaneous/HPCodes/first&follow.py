grammar={'S':['aABb'],'A':['c','epsilon'],'B':['d','epsilon']}
def first(grammar,symbol):
    first_set=set()
    if symbol not in grammar:
        first_set.add(symbol)
        return first_set
    for production in grammar[symbol]:
        if production[0] not in grammar:
            first_set.add(production[0])
        elif production[0] in grammar:
            first_set.update(first(grammar,production[0]))
    return first_set

def follow(grammar,symbol,startsym,follow_set=None):
    if follow_set is None:
        follow_set=set()
    if symbol== startsym:
        follow_set.add('$')
    for key,value in grammar.items():
        for production in value:
            idx=production.find(symbol)
            if idx!=-1:
                if idx<len(production)-1:
                    nextsym=production[idx+1]
                    next_first=first(grammar,nextsym)
                    follow_set.update(next_first-{'epsilon'})
                    if 'epsilon' in next_first:
                        follow_set.update(follow(grammar,key,startsym,follow_set))
                if idx==len(production)-1:
                    if key!=symbol:
                        follow_set.update(follow(grammar,key,startsym,follow_set))
    return follow_set

startsym='S'
print("first(b): ",first(grammar,'B'))
print("\n follow(b):",follow(grammar,'B',startsym))
