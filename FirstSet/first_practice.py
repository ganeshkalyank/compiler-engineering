def first(string):
    first_ = set()
    if string in non_terminals:
        alts = productions[string]

        for alt in alts:
            first_2 = first(alt)
            first_ = first_ | first_2
    elif string in terminals:
        first_ = {string}
    elif string in ['', '#']:
        first_ = {'#'}
    else:
        first_2 = first(string[0])
        if '#' in first_2:
            i = 1
            while '#' in first_2:
                first_ = first_ | (first_2 - {'#'})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'#'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | (first_2 - {'#'})
                i += 1
        else:
            first_ = first_ | first_2
    return first_

terminals = []
non_terminals = []
productions = {}

tc = int(input())
for _ in range(tc):
    terminals.append(input())

ntc = int(input())
for _ in range(ntc):
    non_terminals.append(input())

pc = int(input())
for _ in range(pc):
    prod = input().split('->')
    productions[prod[0]] = prod[1].split('|')

print(productions)

first_set = {}

for nt in non_terminals:
    first_set[nt] = set()

for nt in non_terminals:
    first_set[nt] = first_set[nt] | first(nt)

print(first_set)    
