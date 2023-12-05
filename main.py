import tkinter as tk
import random


class CircleInterface:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.create_circle()

    def create_circle(self):
        size = random.randint(10, 50)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        self.canvas.create_oval(x, y, x + size, y + size, fill=color)

        self.root.after(1000, self.create_circle)  


if __name__ == "__main__":
    root = tk.Tk()
    app = CircleInterface(root)
    root.mainloop()
