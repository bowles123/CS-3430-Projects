# Brian Bowles, Assignment 6, February 28, 2015.
import os,sys
import pygame

PLAYER  = 'smallface.png'
FALCON = 'falcon.png'

GREEN = (0, 255, 0)

class Box(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.speed = 3

    def move(self):
        self.rect.x += self.speed
        
        if self.rect.right > 640:
            self.speed *= -1
        if self.rect.left < 0:
            self.speed *= -1

class Player(pygame.sprite.Sprite):
    def __init__(self, location, speed, image_file):
        self.image = pygame.image.load(image_file).convert_alpha()
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.keydownA = False
        self.keydownD = False
        self.keydownS = False
        self.keydownW = False

    def detectMoving(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.keydownA = True
                if event.key == pygame.K_d:
                    self.keydownD = True
                if event.key == pygame.K_s:
                    self.keydownS = True
                if event.key == pygame.K_w:
                    self.keydownW = True
                if event.key == pygame.K_q:
                    pygame.quit();sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.keydownA = False
                if event.key == pygame.K_d:
                    self.keydownD = False
                if event.key == pygame.K_s:
                    self.keydownS = False
                if event.key == pygame.K_w:
                    self.keydownW = False

    def move(self):
            if self.keydownA == True and self.rect.left > 0:
                self.rect.x -= self.speed
            if self.keydownD == True and self.rect.right < 640:
                self.rect.x += self.speed
            if self.keydownW == True and self.rect.top > 0 :
                self.rect.y -= self.speed
            if self.keydownS == True and self.rect.bottom < 480:
                self.rect.y += self.speed
                
class Control:
    def __init__(self):
        self.falcon1 = Box(FALCON,(400,200))
        self.falcon2 = Box(FALCON,(400,25))
        self.falcon3 = Box(FALCON,(400,375))
        self.player = Player([250,350], 3, PLAYER)
        self.hits = 0
        self.message = "HITS: "
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(self.message, 1, (0, 0, 255))
        self.isColliding = False
        SCREEN.blit(self.text, (300, 0))
        
    def main(self):
        self.player.detectMoving()
        self.player.move()
        self.falcon1.move()
        self.falcon2.move()
        self.falcon3.move()
        SCREEN.fill(GREEN)
        SCREEN.blit(self.falcon1.image, self.falcon1.rect)
        SCREEN.blit(self.falcon2.image, self.falcon2.rect)
        SCREEN.blit(self.falcon3.image, self.falcon3.rect)
        SCREEN.blit(self.player.image, self.player.rect)

        if self.player.rect.colliderect(self.falcon1.rect):
            if self.isColliding == False:
                self.hits = self.hits + 1
                self.isColliding = True
        elif self.player.rect.colliderect(self.falcon2.rect):
            if self.isColliding == False:
                self.hits = self.hits + 1
                self.isColliding = True
        elif self.player.rect.colliderect(self.falcon3.rect):
            if self.isColliding == False:
                self.hits = self.hits + 1
                self.isColliding = True
        else:
            self.isColliding = False
        self.text = self.font.render(self.message + " " + str(self.hits), 1, (0, 0, 255))
        SCREEN.blit(self.text, (320, 0))
        pygame.display.flip()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption("Brian's Collision Detection Game")
    SCREEN = pygame.display.set_mode((640, 480))
    
    run = Control()
    clock = pygame.time.Clock()
    while 1:
        run.main()
        clock.tick(64)
