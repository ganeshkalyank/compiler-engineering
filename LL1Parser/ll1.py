table = {
    'E': {'id': 'TR', '(': 'TR'},
    'R': {'+': '+TR', ')': 'e', '$': 'e'},
    'T': {'id': 'FY', '(': 'FY'},
    'Y': {'+': 'e', '*': '*FY', ')': 'e', '$': 'e'},
    'F': {'id': 'id', '(': '(E)'}
}

inp = 'id + id * id $'
w = inp.split(' ')
i = 0
word = w[i]
stack = []
stack.append('$')
stack.append('E')
focus = stack[1]
terminal = ['*', '+', '*', 'id', '(', ')', 'e', '-', '$']

while focus:
    print('f', focus)
    print('w', word)
    if focus == '$' and word == '$':
        print('input string is valid')
        break
    elif focus in terminal:
        if focus == word:
            print('reduce')
            stack.pop()
            s = len(stack) - 1
            focus = stack[s]
            i = i + 1
            word = w[i]
        else:
            e = stack.pop()
            print(table[e])
            if word not in table[e]:
                print('error')
                break
            if table[e][word]:
                right = table[e][word]
                if right == 'id':
                    stack.append('id')
                else:
                    for j in range(len(right)-1,-1,-1):
                        if(right[j]!='e'):
                            stack.append(right[j])
            print(stack)
    s=len(stack)-1
    focus=stack[s]