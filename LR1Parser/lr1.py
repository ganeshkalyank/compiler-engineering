ACTION = {
    0: {'id': 5, '(': 4},
    1: {'+': 6, '$': '*'},
    2: {'+': -2, '*': 7, ')': -2, '$': -2},
    3: {'+': -4, '*': -4, ')': -4, '$': -4},
    4: {'id': 5, '(': 4},
    5: {'+': -6, '*': -6, ')': -6, '$': -6},
    6: {'id': 5, '(': 4},
    7: {'id': 5, '(': 4},
    8: {'+': 6, ')': 11},
    9: {'+': -1, '*': 7, ')': -1, '$': -1},
    10: {'+': -3, '*': -3, ')': -3, '$': -3},
    11: {'+': -5, '*': -5, ')': -5, '$': -5}
}

GOTO = {
    0: {'E': 1, 'T': 2, 'F': 3},
    4: {'E': 8, 'T': 2, 'F': 3},
    6: {'T': 9, 'F': 3},
    7: {'F': 10}
}

GRAMMAR = [
    None,
    ('E', ['E', '+', 'T']),
    ('E', ['T']),
    ('T', ['T', '*', 'F']),
    ('T', ['F']),
    ('F', ['(', 'E', ')']),
    ('F', ['id'])
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
        for _ in range(2 * len(B)):
            stack.pop()
        stack.append(A)
        stack.append(GOTO[stack[-2]][A])
    else:
        stack.append(sentence[i])
        stack.append(ACTION[stack[-2]][sentence[i]])
        i += 1