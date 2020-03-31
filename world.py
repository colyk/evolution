from tkinter import *
from random import *

mutation_point = 10


class World(Tk):
    def __init__(self, size=35, pixel_size=15):
        super().__init__()
        self.size = size
        self.pixel_size = pixel_size

        self.geometry("{}x{}".format(size * pixel_size, size * pixel_size))
        self.title("Evolution")
        self.resizable(False, False)
        self.c = Canvas(self, width=size * pixel_size, height=size * pixel_size)
        self.c.pack()

    def _draw_cell(self, x0, y0, x1, y1):
        self.c.create_rectangle(x0, y0, x1, y1, fill="#666", width=1, outline="#ccc")

    def draw_world(self):
        x0, y0, x1, y1 = 0, 0, self.pixel_size, self.pixel_size

        for i in range(self.size):
            for j in range(self.size):
                self._draw_cell(x0, y0, x1, y1)
                x0 += self.pixel_size
                x1 += self.pixel_size
            x0 = 0
            y0 += self.pixel_size
            x1 = self.pixel_size
            y1 += self.pixel_size

    def draw_creatures(self, creatures):
        for creature in creatures:
            x0 = creature.x * self.pixel_size
            y0 = creature.y * self.pixel_size
            x1 = x0 + self.pixel_size
            y1 = y0 + self.pixel_size
            self.c.create_rectangle(
                x1, y1, x0, y0, fill="#ff2222", width=1, outline="#ccc"
            )

    def redraw(self):
        # self.update_idletasks()
        self.update()


if __name__ == "__main__":
    w = World()
    w.draw_world()
    w.mainloop()
