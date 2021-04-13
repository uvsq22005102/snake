import tkinter as tk

snake = tk.Tk()
 
canvas_width = 1920
canvas_height = 1080
w = canvas_width // 2
h = canvas_height // 2
canvas = tk.Canvas(snake, width=canvas_width, height=canvas_height)
canvas.pack()
 
r1 = canvas.create_rectangle(w, h, w + 40, h + 10)
t = canvas.create_text(w + 20, h + 5, text="Snake")
 
 
def keypress(event):
    x, y = 0, 0
    if event.char == "q":
        x = -10
    if event.char == "d":
        x = 10
    if event.char == "z":
        y = -10
    if event.char == "s":
        y = 10
    canvas.move(r1, x, y)
    canvas.move(t, x, y)
 
 
snake.bind("<Key>", keypress)
snake.mainloop()

