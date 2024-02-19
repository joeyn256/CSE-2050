def valid_moves(k_idx):
    x = k_idx[0]
    y = k_idx[1]

    #all possible knight move variations across board
    k_moves = [(x + 1,y + 2),(x + 2,y + 1),(x - 1,y + 2),(x + 2,y - 1),(x + 1,y - 2),(x - 2,y + 1),(x - 1,y - 2),(x - 2,y - 1)]
    #all actual possible knight moves
    real_k_moves = []
    for val in k_moves:
        if 0 <= val[0] <= 7 and 0 <= val[1] <= 7:
            real_k_moves.append(val)
    return real_k_moves

def solveable(p_idxs, k_idx, group=None):
    if group is None: group = set()
    #base case
    if len(p_idxs) == len(group):
        return True
    #find valid moves

    valid = valid_moves(k_idx)
    next_moves = set(valid) & p_idxs
    #try valid moves
    for i in next_moves:
        if i not in group:
            new_k_idx = i
            group.add(i)
            if solveable(p_idxs, new_k_idx, group) is False:
                group.remove(i)
            else: 
                return True       
    return False
    #false if 3 false