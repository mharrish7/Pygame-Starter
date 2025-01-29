import pygame 
from settings import * 

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

    def update(self,dt):
        pass

    def draw(self, screen):
        screen.fill(COLORS['blue'])
