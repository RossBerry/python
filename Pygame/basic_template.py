"""
basic_template.py

Basic template for creating an empty display and simple game loop.

"""
__author__ = "Kenneth Berry"
import pygame as pg

# Display size (width, height)
SIZE = (700, 500)
# Window caption
CAPTION = "My Game"
# Define colors
WHITE = (255, 255, 255)


class Game:
    """
    Basic game object.
    """

    def __init__(self, size, caption):
        pg.init()
        self.size = size
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)
        self.done = False
        self.clock = pg.time.Clock()

    def __event_handler(self):
        """
        Handle events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def __update(self):
        """
        Update game objects.
        """
        pass

    def __render(self):
        """
        Render screen to display.
        """
        self.screen.fill(WHITE)
        pg.display.flip()

    def run(self):
        """
        Run main game loop.
        """
        while not self.done:
            self.__event_handler()
            self.__update()
            self.__render()
            self.clock.tick(20)
        pg.quit()


if __name__ == "__main__":
    game = Game(SIZE, CAPTION)
    game.run()
