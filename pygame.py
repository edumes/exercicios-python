import pygame
import os


class Application:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.size = self.width, self.height

    def on_init(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Jogo da Buela')

    def draw(self, pos_x, pos_y):
        pygame.draw.circle(self.screen, (255, 0, 0), (pos_x, pos_y), 50)

    def on_execute(self):
        self.on_init()
        pos_x = int(self.screen.get_size()[0]/2)
        pos_y = int(self.screen.get_size()[1]/2)
        speed = 15

        janela_aberta = True

        while janela_aberta:
            pygame.time.delay(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False

            key_pressed = pygame.key.get_pressed()

            if key_pressed[pygame.K_UP]:
                pos_y -= speed
            if key_pressed[pygame.K_DOWN]:
                pos_y += speed
            if key_pressed[pygame.K_LEFT]:
                pos_x -= speed
            if key_pressed[pygame.K_RIGHT]:
                pos_x += speed

            if pos_y < -45:
                pos_y = 615

            if pos_y > 615:
                pos_y = -30

            print(pos_x)
            if pos_x < -35:
                pos_x = 820

            if pos_x > 835:
                pos_x = -20

            self.screen.fill((0, 0, 0))
            self.draw(pos_x, pos_y)
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    app = Application()
    app.on_execute()
