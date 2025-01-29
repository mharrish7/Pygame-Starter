import pygame 
from settings import  *
from state2 import * 
import sys 


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True 

        self.states = []
        self.splash_screen = SplashScreen(self)
        self.states.append(self.splash_screen)


    def get_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runnig = False 
                pygame.quit()
                sys.exit() 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    INPUTS['escape'] = True 
                    self.running = False 
                elif event.key == pygame.K_w:
                    INPUTS['up'] = True
                elif event.key == pygame.K_s:
                    INPUTS['down'] = True 
                elif event.key == pygame.K_d:
                    INPUTS['right'] = True 
                elif event.key == pygame.K_a:
                    INPUTS['left'] = True
                elif event.key == pygame.K_SPACE:
                    INPUTS['space'] = True 
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    INPUTS['up'] = False
                elif event.key == pygame.K_s:
                    INPUTS['down'] = False 
                elif event.key == pygame.K_d:
                    INPUTS['right'] = False 
                elif event.key == pygame.K_a:
                    INPUTS['left'] = False
                elif event.key == pygame.K_SPACE:
                    INPUTS['space'] = False
 
    def reset_inputs(self):
        for key in INPUTS:
            INPUTS[key] = False 
    
    def loop(self):
        while self.running:
            dt = self.clock.tick(FPS)/1000 
            self.get_inputs()
            self.states[-1].update(dt)
            self.states[-1].draw(self.screen)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.loop() 
