def local_instruction_scheduling(adjacency_matrix, weights, delay):
    n = len(adjacency_matrix)
    cycle = 1
    Ready = set()
    Active = set()
    S = {}
    E = {}

    # Initialize Ready with nodes having no predecessors
    for node in range(n):
        if not any(adjacency_matrix[pred][node] for pred in range(n)):
            Ready.add(node)

    while Ready or Active:
        if Ready:
            # Choose the instruction with the highest weight from Ready
            instr = max(Ready, key=lambda x: weights[x])
            S[instr] = cycle
            Active.add(instr)
            Ready.remove(instr)
        cycle += 1

        for instr in list(Active):
            if S[instr] + delay[instr] <= cycle:
                Active.remove(instr)
                E[instr] = cycle - 1
                for successor in range(n):
                    if adjacency_matrix[instr][successor] and all(pred in S for pred in range(n) if adjacency_matrix[pred][successor]):
                        Ready.add(successor)
        print(Ready,Active)
    return S, E

# Example usage
# Define the weighted adjacency matrix, weights, and delays for instructions
adjacency_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

weights = [13,10,12,9,10,7,8,5,3]  # Define the weights for each instruction
delay = [3,1,3,2,3,2,3,2,3] # Define the delay for each instruction

Start, End = local_instruction_scheduling(adjacency_matrix, weights, delay)
print(f"Start : {Start}\nEnd : {End}")
