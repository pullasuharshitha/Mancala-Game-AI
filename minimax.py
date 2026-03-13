node_count = 0

def minimax(board, depth, maximizing):

    global node_count
    node_count += 1

    if depth == 0 or board.is_game_over():
        return board.evaluate()

    if maximizing:

        best = float('-inf')

        for move in board.get_valid_moves(1):

            child = board.clone()
            child.make_move(move,1)

            val = minimax(child, depth-1, False)
            best = max(best,val)

        return best

    else:

        best = float('inf')

        for move in board.get_valid_moves(0):

            child = board.clone()
            child.make_move(move,0)

            val = minimax(child, depth-1, True)
            best = min(best,val)

        return best