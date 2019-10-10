import pygame
from network import Network
from player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Battleship the Game - Client")

# client_number = 0
#
#
# def read_pos(string):  # Helper function
#     string = string.split(",")
#     return int(string[0]), int(string[1])
#
#
# def make_pos(tup):  # Helper function
#     return str(tup[0]) + "," + str(tup[1])



def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    # start_pos = read_pos(n.get_pos())
    # p = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))
    # p2 = Player(0, 0, 100, 100, (255, 0, 0))
    p = n.get_p()

    clock = pygame.time.Clock()

    while run:

        clock.tick(60)
        p2 = n.send(p)
        # p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
        # p2.x = p2_pos[0]
        # p2.y = p2_pos[1]
        # p2.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(win, p, p2)


main()
