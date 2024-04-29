from collections import deque

table = {
    "E" : {
        "id" : ["T", "E1"],
        "(" : ["T", "E1"]
    },
    "E1" : {
        "+" : ["+", "T", "E1"],
        ")" : [""],
        "$" : [""]
    },
    "T" : {
        "id" : ["F", "T1"],
        "(" : ["F", "T1"]
    },
    "T1" : {
        "+" : [""],
        "*" : ["*", "F", "T1"],
        ")" : [""],
        "$" : [""]
    },
    "F" : {
        "id" : ["id"],
        "(" : ["(", "E", ")"]
    }
}

stack = ["$", "E"]
terminals = {"id", "+", "*", "(", ")", "$"}
inputstr = deque(input("Enter the input statement:\n").split())
inputstr.append("$")

while True:
    try:
        if stack[-1] == "$" and inputstr[0] == "$":
            print("Success!!")
            break
        elif stack[-1] in terminals:
            if stack[-1] == inputstr[0]:
                stack.pop()
                inputstr.popleft()
            else:
                print(stack[-1], inputstr[0])
                print("Failure!!")
                break
        else:
            x = stack.pop()
            stack.extend(filter(None, table[x][inputstr[0]][::-1]))
    except:
        print("Failure!!")
        break
