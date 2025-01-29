import pygame 
from settings import * 
from characters import * 

class State:
    def __init__(self,game):
        self.game = game
        self.prev_state = None 

    def update(self, dt):
        pass 
    def draw(self, screen):
        pass

    def enter_state(self):
        if len(self.game.states) > 1:
            self.prev_state = self.game.states[-1]
        self.game.states.append(self)
    
    def exit_state(self):
        self.game.states.pop()
















































        

class SplashScreen(State):
    def __init__(self, game):
        State.__init__(self,game)
    
    def update(self,dt):
        if INPUTS['space']:
             Scene(self.game).enter_state()
             self.game.reset_inputs()


    def draw(self, screen):
        screen.fill(COLORS['white']) 


class Scene(State):
    def __init__(self, game):
        State.__init__(self,game)

        self.update_sprites = pygame.sprite.Group()
        self.drawn_sprites = pygame.sprite.Group()

        self.player = Player(game,self,[self.update_sprites,self.drawn_sprites],(WIDTH/2,HEIGHT/2),'player')
    
    def update(self,dt):
        self.update_sprites.update(dt)

    def draw(self, screen):
        screen.fill(COLORS['blue'])
        self.drawn_sprites.draw(screen)