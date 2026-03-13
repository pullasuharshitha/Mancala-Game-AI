from board import MancalaBoard
import minimax
import alphabeta
import ui
from compare import show_graph

board = MancalaBoard()

DEPTH = 5

while not board.is_game_over():

    ui.draw_board(board)

    # ---------- HUMAN MOVE ----------
    human_move = ui.get_human_move(board)
    board.make_move(human_move,0)

    if board.is_game_over():
        break

    # ---------- AI MOVE ----------
    best_val = float('-inf')
    best_move = None

    for move in board.get_valid_moves(1):

        new_board = board.clone()
        new_board.make_move(move,1)

        # Alpha Beta for AI decision
        val = alphabeta.alphabeta(new_board,DEPTH,-9999,9999,False)

        # Run minimax only for node comparison
        minimax.minimax(new_board,DEPTH,False)

        if val > best_val:
            best_val = val
            best_move = move

    board.make_move(best_move,1)

# ---------- GAME OVER ----------

human_remaining = sum(board.board[0:6])
ai_remaining = sum(board.board[7:13])

board.board[6] += human_remaining
board.board[13] += ai_remaining

human_score = board.board[6]
ai_score = board.board[13]

print("\nFinal Scores")
print("Human:", human_score)
print("AI:", ai_score)

if human_score > ai_score:
    winner = "Human Wins!"
elif ai_score > human_score:
    winner = "AI Wins!"
else:
    winner = "Draw!"

print(winner)

print("\nMinimax nodes:", minimax.node_count)
print("AlphaBeta nodes:", alphabeta.node_count_ab)

# ---------- GRAPH ----------
show_graph(minimax.node_count, alphabeta.node_count_ab)

# ---------- RESULT SCREEN ----------
ui.show_winner(winner, human_score, ai_score)