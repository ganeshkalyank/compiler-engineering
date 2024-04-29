ACTION = {
    0 : {'a' : 3, 'b' : 4},
    1 : {'$' : '*'},
    2 : {'a' : 6, 'b' : 7},
    3 : {'a' : 3, 'b' : 4},
    4 : {'a' : -3, 'b' : -3},
    5 : {'$' : -1},
    6 : {'a' : 6, 'b' : 7},
    7 : {'$' : -3},
    8 : {'a' : -2, 'b' : -2},
    9 : {'$' : -2}
}
GOTO = {
    0 : {'S' : 1, 'A' : 2},
    2 : {'A' : 5},
    3 : {'A' : 8},
    6 : {'A' : 9}
}
GRAMMAR = [
    None,
    ('S' , ['A', 'A']),
    ('A' , ['a', 'A']),
    ('A' , ['b'])
]
sentence = input("Enter the statement: ").strip().split()
stack = ['$', 0]
i = 0
while True:
    if i >= len(sentence) or sentence[i] not in ACTION[stack[-1]]:
        print("Failed!!")
        break
    if ACTION[stack[-1]][sentence[i]] == '*':
        print("Success!!")
        break
    elif ACTION[stack[-1]][sentence[i]] < 0:
        A, B = GRAMMAR[-ACTION[stack[-1]][sentence[i]]]
        for _ in range(2*len(B)):
            stack.pop()
        stack.append(A)
        stack.append(GOTO[stack[-2]][A])
    else:
        stack.append(sentence[i])
        stack.append(ACTION[stack[-2]][sentence[i]])
        i += 1
