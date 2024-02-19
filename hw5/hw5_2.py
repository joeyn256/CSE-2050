import itertools

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
    
def solveable(p_idxs, k_idx):
    # keep intital knight position
    initial_knight_pos = (k_idx[0], k_idx[1])
    #need to also save how many pawns need to get taken
    pawns_left = len(p_idxs)
    # easy way to permute through all combinations of pawn sequences
    pawns_pos_seq = itertools.permutations(p_idxs)

    # go through each sequence
    for sequences in pawns_pos_seq:
        sequences = list(sequences)  # convert set to list
        knight_moves = 0 #need to set the night moves to 0
        knight_move_list = [k_idx] # have the first value saved in the knight move list
        knight_pos = initial_knight_pos  # Saving initial position of knight to start again
        
        for i in range(len(sequences)): #Have no idea the length of sequences, so must take range of it
            valid_knight_moves = valid_moves(knight_pos)
            for val in valid_knight_moves:
                if((val[0],val[1]) in sequences):
                    knight_moves +=1
                    knight_move_list.append(((val[0], val[1])))
                    # removes the first occurrence of an element from a list
                    sequences.remove((val[0],val[1]))
                    knight_pos = val # I understand we should be using recursion, but it is not exactly necessary for this problem since I have all possible permutations; I think my method is also more mempory efficient
                    break

        if(knight_moves==pawns_left): # base case says if the knight has the number of possible moves as there are pawns then all must be removed
            return True
        else: # if not then the statement is false
            return False

'''
    formatting the chess board
    create empty chess board
    rows, cols = (8, 8)
    chess_board = [['-' for i in range(cols)] for j in range(rows)]

    t = ''
    for n in range(8):
        for m in range(8):
            t = t + chess_board[n][m]
        t = t + '\n'
    t = t.strip('\n')
    print(t)

    q = [[1,2,3,4,5],[6,7,8,9,10]]
    print(q)
'''

