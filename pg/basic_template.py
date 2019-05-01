"""
basic_template.py

Basic PyGame template for creating a simple game loop that displays a blank white screen.

"""
__author__ = "Kenneth Berry"

import pygame as pg


DISPLAY_SIZE = (700, 500)  # Display window size (width, height)
CAPTION = "My Game"        # Display window caption

# Constant Colors:
WHITE = (255, 255, 255)    #(Red, Green, Blue)


class Game:
    """
    Basic game loop object.
    """

    def __init__(self, size, caption):
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)
        self.window_size = size
        self.done = False  # Flag for exiting game loop
        self.clock = pg.time.Clock()  # Clock to help controll frames per second

    def event_handler(self):
        """
        Handle events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            #-- Add event handling code here --#

    def update(self):
        """
        Update game objects.
        """
        #-- Add game updates and logic here --#

    def render(self):
        """
        Render screen to display.
        """
        self.screen.fill(WHITE)  # Fill background before drawing scene
        #-- Add rendering code here --#

        #-----------------------------#
        pg.display.flip()  # Draw the screen onto the display window

    def run(self):
        """
        Run main game loop.
        """
        while not self.done:
            self.event_handler()
            self.update()
            self.render()
            self.clock.tick(20)


if __name__ == "__main__":
    pg.init()
    GAME = Game(DISPLAY_SIZE, CAPTION)
    GAME.run()
    pg.quit()
