import pygame
from Assets.Cards import PlayerCard

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.inGame = False
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.size = (self.screen.get_width(), self.screen.get_height())
        pygame.display.set_caption("The binding of isaac Four Souls")

        # Ticks

        self.clock = pygame.time.Clock()
        self.fps = 120

        # players
        self.rojo = PlayerCard(690, 559, 60, 96, (255, 0, 0) , False)
        self.amarillo = PlayerCard(1290, 114, 60, 96, (255, 255, 255) , True)
        self.azul = PlayerCard(11, 559, 60, 96, (0, 0, 255) , False)
        self.verde = PlayerCard(611, 114, 60, 96, (0, 255, 0) , True)

        # config
        self.players = []

    def load_resources(self):
        self.bg = pygame.image.load("Resources/Images/table.png")
        self.bg = pygame.transform.scale(self.bg, self.size)
        self.monsters = pygame.image.load("Resources/Cards/monster_card_back.png")
        self.monsters = pygame.transform.scale(self.monsters, (60, 96))
        
        

    def run(self):
        self.inGame = True
        self.load_resources()
        while self.inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.inGame = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.rojo.add_player_card()
                        
                    if event.key == pygame.K_s:
                        self.amarillo.add_player_card()
                    if event.key == pygame.K_d:
                        self.azul.add_player_card()
                    if event.key == pygame.K_f:
                        self.verde.add_player_card()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.inGame = False
                
            # if keys[pygame.K_a]:
                

            print(pygame.mouse.get_pos())

            # screen
            pygame.display.flip()
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.monsters, (1231,336))

            
            
            self.rojo.draw(self.screen)
            self.amarillo.draw(self.screen)
            self.azul.draw(self.screen)
            self.verde.draw(self.screen)


            # ticks
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
