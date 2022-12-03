#import environment
import pygame

pygame.init()

#setting value
width = 4
height = 3
size = 250

#value
width = width*size  #zoom size
height = height*size  #zoom size
ratio = (width/480 + height/360)/2  #width/480 == height/360 == average(width/480, height/360)

#create windown
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('2D Game')

#frame
FPS = 60
clock = pygame.time.Clock()

#color value
red = (255, 0, 0)  #color RGB
black = (0, 0, 0)  #color RGB

#function
class player():
    def __init__(self, type_move, x, y, width, height, speed, color):
        self.type_move = type_move
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def draw_player(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def control_player(self):
        keys = pygame.key.get_pressed()

        if self.type_move == 'arrow':
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
            if keys[pygame.K_LEFT]:
                self.x -= self.speed

#create player
player_a = player('arrow', ratio*100, ratio*100, ratio*20, ratio*20, ratio*3, red)

def draw():
    win.fill(black)

    #draw player
    player_a.draw_player()

    pygame.display.update()

def control():
    player_a.control_player()

def main():
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()
        control()

    pygame.quit()

#run
if __name__=="__main__":
    main()
