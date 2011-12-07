import pygame, random
import math, sys

class Dot(object):
    """Dot object"""
    def __init__(self):
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

class Projectile(object):
    def __init__(self):
        self.surf = pygame.image.load("shuriken0.png").convert_alpha()
        self.rect = pygame.Rect(0, 0, 24, 24)
        
class MissileDown(object): #Missle flys down from the top.
    def __init__(self):
        self.surf = pygame.image.load("MissileD.png").convert_alpha()
        self.rect = pygame.Rect(0, 0, 20, 20)
        
class MissileUp(object): #Missile comes from the top.
    def __init__(self):
        self.surf = pygame.image.load("MissileU.png").convert_alpha()
        self.rect = pygame.Rect(0, 0, 20, 20)
        
class MissileRight(object): #Missile comes from the right
    def __init__ (self):
        self.surf = pygame.image.load("MissileR.png").convert_alpha()
        self.rect = pygame.Rect(0, 0, 20, 20)
        
class Monster(object):
    def __init__(self) :
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 100, 0))
        self.rect = pygame.Rect(0, 0, 25, 25)
        
class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((0, 0, 0))
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.keymap = [False, False, False, False] #up = 0, down = 1, left = 2, right = 3
        self.arrowmap = [False, False, False, False] #up = 0, down = 1, left = 2,, right = 3
        self.starspawn = [False, False, False, False] #up = 0, ,sown = 1, left = 2, right = 3
        self.missiledownspawn = True #
        self.missileupspawn = True #
        self.dot = Dot()
        self.dot.rect.topleft = (400, 300)
            
        self.projectile_list = [Projectile() for y in range(1)]
        for projectile in self.projectile_list:
            projectile.rect.topleft = (375, 300)
        
        self.dmiss = MissileDown()
        self.dmiss.rect.center = (200, 0)
        
        self.umiss = MissileUp()
        self.umiss.rect.center = (400, 400)
        
        self.m1 = Monster()
        self.m1.rect.center = (100, 100)
        self.m2 = Monster()
        self.m2.rect.center = (700, 500)
        self.m3 = Monster()
        self.m3.rect.center = (100, 500)

        #self.dot.rect.bottomright = (345, 200)
        
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    
                #testing for the block
                if event.key == pygame.K_d:
                    self.keymap[3] = True
                if event.key == pygame.K_a: 
                    self.keymap[2] = True
                if event.key == pygame.K_s:
                    self.keymap[1] = True
                if event.key == pygame.K_w:
                   self.keymap[0] = True      
                   
                # Testing for the ninja star
                
                if event.key == pygame.K_i:
                    for projectile in self.projectile_list:
                        projectile.rect.topleft = (self.dot.rect.x, self.dot.rect.y)
                    self.arrowmap[0] = True
                    self.arrowmap[1] = False
                    self.arrowmap[2] = False
                    self.arrowmap[3] = False
                if event.key == pygame.K_k:
                    for projectile in self.projectile_list:
                        projectile.rect.topleft = (self.dot.rect.x, self.dot.rect.y)
                    self.arrowmap[0] = False
                    self.arrowmap[1] = True
                    self.arrowmap[2] = False
                    self.arrowmap[3] = False
                if event.key == pygame.K_l:
                    for projectile in self.projectile_list:
                        projectile.rect.topleft = (self.dot.rect.x, self.dot.rect.y)
                    self.arrowmap[0] = False
                    self.arrowmap[1] = False
                    self.arrowmap[2] = True
                    self.arrowmap[3] = False
                if event.key == pygame.K_j:
                    for projectile in self.projectile_list:
                        projectile.rect.topleft = (self.dot.rect.x, self.dot.rect.y)
                    self.arrowmap[0] = False
                    self.arrowmap[1] = False
                    self.arrowmap[2] = False
                    self.arrowmap[3] = True
                    
                #   Starspawn Test KEYDOWN
                #   Spawns nstar back at original position
                if event.key == pygame.K_i:
                    self.starspawn[0] = False
                if event.key == pygame.K_k:
                    self.starspawn[1] = False
                if event.key == pygame.K_j:
                    self.starspawn[2] = False
                if event.key == pygame.K_l:
                    self.starspawn[3] = False
                    
            if event.type == pygame.KEYUP:
                #    Block KEYUP test
                if event.key == pygame.K_d:
                    self.keymap[3] = False
                if event.key == pygame.K_a:
                    self.keymap[2] = False
                if event.key == pygame.K_s:
                    self.keymap[1] = False
                if event.key == pygame.K_w:
                    self.keymap[0] = False
                    
                #   starspawn KEYUP test
                if event.key == pygame.K_i:
                    self.starspawn[0] = True
                if event.key == pygame.K_k:
                    self.starspawn[1] = True
                if event.key == pygame.K_j:
                    self.starspawn[2] = True
                if event.key == pygame.K_l:
                    self.starspawn[3] = True
     
        
    def update(self):
        if self.keymap[0] == True: #up block
            future_dot = self.dot.rect.move(0, -10)
            if self.screen.get_rect().contains(future_dot):
                self.dot.rect = future_dot
            else:
                self.dot.rect.top = 0
        
        if self.keymap[1] == True: #down block
            future_dot = self.dot.rect.move(0, 10)
            if self.screen.get_rect().contains(future_dot):
                self.dot.rect = future_dot
            else:
                self.dot.rect.bottom = 600
                    
        if self.keymap[2] == True: #left block
            future_dot = self.dot.rect.move(-10, 0)
            if self.screen.get_rect().contains(future_dot):
                self.dot.rect = future_dot
            else:
                self.dot.rect.left = 0
        
        if self.keymap[3] == True: #right block
            future_dot = self.dot.rect.move(10, 0)
            if self.screen.get_rect().contains(future_dot):
                self.dot.rect = future_dot
            else:
                self.dot.rect.right = 800
                    
        if self.arrowmap[0] == True: #up ninja star
            for projectile in self.projectile_list:
                future_proj = projectile.rect.move(0, -18)
                projectile.rect = future_proj
                
        if self.arrowmap[1] == True: #down ninja star
            for projectile in self.projectile_list:
                future_proj = projectile.rect.move(0, 18)
                projectile.rect = future_proj
                
        if self.arrowmap[2] == True: #left ninja star
            for projectile in self.projectile_list:
                future_proj = projectile.rect.move(18, 0)
                projectile.rect = future_proj
                
        if self.arrowmap[3] == True: #right ninja star
            for projectile in self.projectile_list:
                future_proj = projectile.rect.move(-18, 0)
                projectile.rect = future_proj
        
        # moving mobs towards player
        a = (self.dot.rect.x - self.m1.rect.x) / 30
        b = (self.dot.rect.y - self.m1.rect.y) / 30
        future_m1 = self.m1.rect.move(a, b)
        self.m1.rect = future_m1
        for projectile in self.projectile_list:
            if self.m1.rect.colliderect(projectile):
                if self.arrowmap[0] == True:
                    hit_m1 = self.m1.rect.move(0, -100)
                    self.m1.rect = hit_m1
                if self.arrowmap[1] == True:
                    hit_m1 = self.m1.rect.move(0, 100)
                    self.m1.rect = hit_m1
                if self.arrowmap[2] == True:
                    hit_m1 = self.m1.rect.move(100, 0)
                    self.m1.rect = hit_m1
                if self.arrowmap[3] == True:
                    hit_m1 = self.m1.rect.move(-100, 0)
                    self.m1.rect = hit_m1
        
        
        # move mob at position player - 2, player - 2.
        a = (self.dot.rect.x - self.m2.rect.x) / 20
        b = (self.dot.rect.y - self.m2.rect.y) / 20
        future_m2 = self.m2.rect.move(a - 2, b - 2)
        self.m2.rect = future_m2
        for projectile in self.projectile_list:
            if self.m2.rect.colliderect(projectile):
                if self.arrowmap[0] == True:
                    hit_m2 = self.m2.rect.move(0, -100)
                    self.m2.rect = hit_m2
                if self.arrowmap[1] == True:
                    hit_m2 = self.m2.rect.move(0, 100)
                    self.m2.rect = hit_m2
                if self.arrowmap[2] == True:
                    hit_m2 = self.m2.rect.move(100, 0)
                    self.m2.rect = hit_m2
                if self.arrowmap[3] == True:
                    hit_m2 = self.m2.rect.move(-100, 0)
                    self.m2.rect = hit_m2
         
         # move mob at position player + 2, player + 2
        a = (self.dot.rect.x - self.m3.rect.x) / 20
        b = (self.dot.rect.y - self.m3.rect.y) / 20
        future_m3 = self.m3.rect.move(a + 2, b + 2)
        self.m3.rect = future_m3
        for projectile in self.projectile_list:
            if self.m3.rect.colliderect(projectile):
                if self.arrowmap[0] == True:
                    hit_m3 = self.m3.rect.move(0, -100)
                    self.m3.rect = hit_m3
                if self.arrowmap[1] == True:
                    hit_m3 = self.m3.rect.move(0, 100)
                    self.m3.rect = hit_m3
                if self.arrowmap[2] == True:
                    hit_m3 = self.m3.rect.move(100, 0)
                    self.m3.rect = hit_m3
                if self.arrowmap[3] == True:
                    hit_m3 = self.m3.rect.move(-100, 0)
                    self.m3.rect = hit_m3
        
          # Fires a missle down
        f_dmissile = self.dmiss.rect.move(0, 10)
        if self.screen.get_rect().contains(f_dmissile):
            self.dmiss.rect = f_dmissile
        else:
            if (self.missiledownspawn == True):
                a = 600 * random.random()
                b = int(a)
                self.dmiss.rect.center = (b, 0)
            else:
                self.dmiss.rect.center = (600, 0)
        
        f_umissile = self.umiss.rect.move(0, -10)
        if self.screen.get_rect().contains(f_umissile):
            self.umiss.rect = f_umissile
        else:
            if (self.missileupspawn == True):
                c = 600 * random.random()
                d = int(c)
                self.umiss.rect.center = (d, 600)
            else:
                self.umiss.rect.center = (400, 800)
                
    def draw(self):
        self.screen.fill((3, 255, 3))
        #self.screen.blit(self.dot, self.dot_rect)
        self.screen.blit(self.dot.surf, self.dot.rect)
            
        for projectile in self.projectile_list:
            self.screen.blit(projectile.surf, projectile.rect)
        
        self.screen.blit(self.m1.surf, self.m1.rect)
        self.screen.blit(self.m2.surf, self.m2.rect)
        self.screen.blit(self.m3.surf, self.m3.rect)
        
        self.screen.blit(self.dmiss.surf, self.dmiss.rect)
        self.screen.blit(self.umiss.surf, self.umiss.rect)
        
        
pygame.init()
g = Game()
while not g.game_over:
    g.clock.tick(30)
    g.process_input()
    g.update()
    g.draw()
    pygame.display.flip()
sys.exit()
