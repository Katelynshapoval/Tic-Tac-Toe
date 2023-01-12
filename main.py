import pygame
pygame.init()
pygame.display.set_caption("Tic Tac Toe")
win = pygame.display.set_mode((500,480))

# Images
bg = pygame.image.load('bg.jpg')

cross_pic = pygame.image.load("cross.png")
cross_pic = pygame.transform.scale(cross_pic, (70, 70))

circle_pic = pygame.image.load("circle.png")
circle_pic = pygame.transform.scale(circle_pic, (70, 70))

class Board():
    def __init__(self, x, y, width, height, color):
        self.positions = {}
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.num = 0

    def draw(self):
        self.num = 0
        # Lines
        for x in range(1, 4):
        # Columns
            for y in range(1, 4):
                self.num += 1
                # Draw a square
                pygame.draw.rect(win, (0,0,0), (self.x + self.width * y, self.y + self.height * x, self.width, self.height), 2)
                # Add its position to a dict
                self.positions[self.num] = [self.x + self.width * y, self.y + self.height * x]

class Character():
    def __init__(self, x, y, image = ""):
        self.positions = {}
        self.image = image
        self.x = x
        self.y = y
    # Makes it easy for me to call a func. I don't need to use an object (cross, circle)
    @classmethod
    # For lines
    def draw_line(cl, line):
        # Oh..
        start_x = 144
        start_y = 120
        mid_x = 144
        mid_y = 190
        end_x = 284
        end_y = 120
        # Decided where to draw a line based on a winning combination
        if line == 0:
            start_pos = (start_x, start_y + 35)
            end_pos = (end_x + 70, end_y + 35)
        elif line == 1:
            start_pos = (start_x, mid_y + 35)
            end_pos = (end_x + 70, end_y + 105)
        elif line == 2:
            start_pos = (start_x, mid_y + 105)
            end_pos = (end_x + 70, end_y + 175)
        elif line == 3:
            start_pos = (start_x, start_y)
            end_pos = (start_x + 70 * 3, start_y + 70 * 3)
        elif line == 4:
            start_pos = (start_x + 70 * 3, start_y)
            end_pos = (start_x, start_y + 70 * 3)
        elif line == 5:
            start_pos = (start_x + 35, start_y)
            end_pos = (start_x + 35, end_y + 70 * 3)
        elif line == 6:
            start_pos = (start_x + 35 + 70, start_y)
            end_pos = (start_x + 35 + 70, end_y + 70 * 3)
        elif line == 7:
            start_pos = (start_x + 35 + 140, start_y)
            end_pos = (start_x + 35 + 140, end_y + 70 * 3)
        
        # Draws a line
        pygame.draw.line(win, pygame.Color("red"), start_pos, end_pos, 3)
    @classmethod    
    def sleep_sec(cl):
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
    # For cross and circle
    def draw(self):
        win.blit(self.image, (self.x, self.y))

def redrawGameWindow(line_n):
    win.blit(bg, (0,0))
    cross_score_text = font.render("Cross: " + str(cross_score), 1, (255,255,255))
    win.blit(cross_score_text, (380, 10))
    circle_score_text = font.render("Circle: " + str(circle_score), 1, (255,255,255))
    win.blit(circle_score_text, (20, 10))
    for cross in crosses:
        cross.draw()
    for circle in circles:
        circle.draw()
    # Draws a line only of there is a winner
    if winner != "":
        Character.draw_line(line_n)
    board.draw()
    
    pygame.display.update()
    
    return board.positions

def check_win(cross_pos, circle_pos):
    # Line and winner are undefined
    winner = ""
    line = 0
    # Winning combinations
    winn = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
    for l in winn:
        # 3 points = winner
        points_cross = 0
        points_circle = 0
        # For crosses
        for pos in l:
            if pos in cross_pos:
                points_cross += 1
                if points_cross == 3:
                    winner = "Cross"
                    # Get an index of a combination
                    line = winn.index(l)
                    break
            else: 
                points_cross = 0
        # For circles
        for pos in l:
            if pos in circle_pos:
                points_circle += 1
                if points_circle == 3:
                    winner = "Circle"
                    # Get an index of a combination
                    line = winn.index(l)
                    break
            else: 
                points_circle = 0
    return winner, line

# Variables

font = pygame.font.SysFont("comicsans", 30, True)
# A number of the winning combination
line_n = 0
# Score
cross_score = 0
circle_score = 0
# Name of the winner (cross, circle)
winner = ""
board = Board(74, 50, 70, 70, "black")
# All the characters
crosses = []
circles = []
# The positions of the characters on the board (1, 2, 3...). 
# Should have created a dict and combine positions and characters
cross_pos = []
circle_pos = []
# Positions which are taken
busy = []
cross_turn = True
circle_turn = False
run = True
# List of square positions
pos_list = redrawGameWindow(line_n)


while run:
    if winner != "" or len(busy) == 9:
        Character.sleep_sec()
        winner = ""
        busy = []
        crosses = []
        circles = []
        cross_pos = []
        circle_pos = []
        cross_turn = True
        circle_turn = False
        line_n = 0
        pos_list = redrawGameWindow(line_n)

    # If user clicked on "X", game closes without an error 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # If user clicked somewhere
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            # Condition will prevent user from playing after someone wins
            if winner == "":
                # For every square in dictionary
                for pos_square in range(1, len(pos_list) + 1):
                    # If position is not taken
                    if pos_square not in busy:
                        # Checks x
                        if pos_list[pos_square][0] <= x and pos_list[pos_square][0] + 70 >= x:
                            # Checks y
                            if pos_list[pos_square][1] <= y and pos_list[pos_square][1] + 70>= y:
                                # Makes the position busy
                                busy.append(pos_square)
                                # Coord. where character will be drawn
                                x = pos_list[pos_square][0]
                                y = pos_list[pos_square][1]
                                # If it's cross's turn
                                if cross_turn == True:
                                    # Create a cross
                                    cross = Character(x, y, cross_pic)
                                    # Add to the list of crosses
                                    crosses.append(cross)
                                    # Switch turns
                                    cross_turn = False
                                    circle_turn = True
                                    # Add position
                                    cross_pos.append(pos_square)
                                # If it's circle's turn
                                elif circle_turn == True:
                                    # Create a circle
                                    circle = Character(x, y, circle_pic)
                                    # Add to list of circles
                                    circles.append(circle)
                                    # Switch turns
                                    cross_turn = True
                                    circle_turn = False
                                    # Add position
                                    circle_pos.append(pos_square)
                                # Get the winner if there is and line
                                winner, line_n = check_win(cross_pos, circle_pos)
                                if winner == "Cross":
                                    cross_score += 1
                                elif winner == "Circle":
                                    circle_score += 1
            
    redrawGameWindow(line_n)

pygame.quit()