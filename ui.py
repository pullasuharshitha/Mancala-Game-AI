import pygame
import sys

pygame.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mancala AI")

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 50)

human_pits = [(200 + i*90,350) for i in range(6)]
ai_pits = [(200 + i*90,150) for i in range(6)]

# -------- DRAW STONES --------
def draw_stones(x,y,count):

    for i in range(count):

        pygame.draw.circle(
            screen,
            (255,215,0),
            (x + (i%3)*12 -10, y + (i//3)*12 -10),
            6
        )

# -------- DRAW BOARD --------
def draw_board(board):

    screen.fill((30,120,30))

    # Human pits
    for i,(x,y) in enumerate(human_pits):
        pygame.draw.circle(screen,(139,69,19),(x,y),45)
        draw_stones(x,y,board.board[i])

    # AI pits
    for i,(x,y) in enumerate(ai_pits):
        pygame.draw.circle(screen,(139,69,19),(x,y),45)
        draw_stones(x,y,board.board[7+i])

    # Human store
    pygame.draw.rect(screen,(160,82,45),(40,120,80,260))
    draw_stones(80,250,board.board[6])

    # AI store
    pygame.draw.rect(screen,(160,82,45),(780,120,80,260))
    draw_stones(820,250,board.board[13])

    pygame.display.update()

# -------- HUMAN MOVE --------
def get_human_move(board):

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mx,my = pygame.mouse.get_pos()

                for i,(x,y) in enumerate(human_pits):

                    dist = ((mx-x)**2 + (my-y)**2)**0.5

                    if dist < 45 and board.board[i] > 0:
                        return i

# -------- SHOW FINAL RESULT --------
def show_winner(winner_text, human_score, ai_score):

    screen.fill((30,120,30))

    title = big_font.render(winner_text, True, (255,255,255))
    title_rect = title.get_rect(center=(WIDTH//2, 140))

    human_text = font.render(f"Human Score: {human_score}", True, (255,255,255))
    ai_text = font.render(f"AI Score: {ai_score}", True, (255,255,255))

    human_rect = human_text.get_rect(center=(WIDTH//2, 240))
    ai_rect = ai_text.get_rect(center=(WIDTH//2, 300))

    screen.blit(title, title_rect)
    screen.blit(human_text, human_rect)
    screen.blit(ai_text, ai_rect)

    pygame.display.update()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()