import tkinter as tk
import random

root = tk.Tk()
root.title("Breakout Game")
canvas = tk.Canvas(root, width=500, height=400, bg="black")
canvas.pack()

paddle = canvas.create_rectangle(200, 380, 300, 390, fill="white")
ball = canvas.create_oval(240, 360, 260, 380, fill="red")
ball_dx = 3
ball_dy = -3

bricks = []
for i in range(5):
    for j in range(10):
        brick = canvas.create_rectangle(5 + j*50, 5 + i*20, 50 + j*50, 25 + i*20, fill="blue")
        bricks.append(brick)

def move_paddle(event):
    x = event.x
    canvas.coords(paddle, x - 50, 380, x + 50, 390)

canvas.bind("<Motion>", move_paddle)

def game_loop():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    pos = canvas.coords(ball)

    if pos[0] <= 0 or pos[2] >= 500:
        ball_dx = -ball_dx
    if pos[1] <= 0:
        ball_dy = -ball_dy
    if pos[3] >= 400:
        canvas.create_text(250, 200, text="Game Over", fill="white", font=("Helvetica", 24))
        return

    paddle_pos = canvas.coords(paddle)
    if pos[3] >= paddle_pos[1] and paddle_pos[0] < pos[0] < paddle_pos[2]:
        ball_dy = -ball_dy

    for brick in bricks:
        if canvas.coords(brick):
            brick_pos = canvas.coords(brick)
            if brick_pos[0] < pos[2] and brick_pos[2] > pos[0] and brick_pos[1] < pos[3] and brick_pos[3] > pos[1]:
                canvas.delete(brick)
                bricks.remove(brick)
                ball_dy = -ball_dy
                break

    if not bricks:
        canvas.create_text(250, 200, text="You Win!", fill="yellow", font=("Helvetica", 24))
        return

    root.after(20, game_loop)

game_loop()
root.mainloop()
