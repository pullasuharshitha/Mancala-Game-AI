node_count_ab = 0

def alphabeta(board, depth, alpha, beta, maximizing):

    global node_count_ab
    node_count_ab += 1

    if depth == 0 or board.is_game_over():
        return board.evaluate()

    if maximizing:

        value = float('-inf')

        for move in board.get_valid_moves(1):

            child = board.clone()
            child.make_move(move,1)

            value = max(value,
                        alphabeta(child, depth-1, alpha, beta, False))

            alpha = max(alpha,value)

            if alpha >= beta:
                break

        return value

    else:

        value = float('inf')

        for move in board.get_valid_moves(0):

            child = board.clone()
            child.make_move(move,0)

            value = min(value,
                        alphabeta(child, depth-1, alpha, beta, True))

            beta = min(beta,value)

            if alpha >= beta:
                break

        return value