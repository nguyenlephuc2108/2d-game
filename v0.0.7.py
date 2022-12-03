#import environment
import pygame

pygame.init()

#setting value
width = 4
height = 3
size = 250
smoothness = 15

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
blue = (0, 0, 255)  #color RGB

#function
class player():
    def __init__(self, type_move, xn, yn, width, height, speed, color):
        self.type_move = type_move
        self.xn = xn
        self.yn = yn
        self.xl = xn
        self.yl = yn
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def draw_player(self):
        pygame.draw.rect(win, self.color, (self.xn, self.yn, self.width, self.height))

    def control_player(self):
        keys = pygame.key.get_pressed()

        player_rect = pygame.Rect(self.xl, self.yl, self.width, self.height)

        if self.type_move == 'arrow':
            if keys[pygame.K_UP]:
                player_rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                player_rect.y += self.speed
            if keys[pygame.K_RIGHT]:
                player_rect.x += self.speed
            if keys[pygame.K_LEFT]:
                player_rect.x -= self.speed

        if self.type_move == 'wasd':
            if keys[pygame.K_w]:
                player_rect.y -= self.speed
            if keys[pygame.K_s]:
                player_rect.y += self.speed
            if keys[pygame.K_d]:
                player_rect.x += self.speed
            if keys[pygame.K_a]:
                player_rect.x -= self.speed

        player_rect.clamp_ip(win.get_rect())
        self.xl = player_rect.x
        self.yl = player_rect.y

        self.xn += (self.xl-self.xn)/smoothness
        self.yn += (self.yl-self.yn)/smoothness

#create player
player_a = player('arrow', ratio*100, ratio*100, ratio*20, ratio*20, ratio*3, red)
player_b = player('wasd', ratio*200, ratio*100, ratio*20, ratio*20, ratio*3, blue)

def draw():
    win.fill(black)

    #draw player
    player_a.draw_player()
    player_b.draw_player()

    pygame.display.update()

def control():
    player_a.control_player()
    player_b.control_player()

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