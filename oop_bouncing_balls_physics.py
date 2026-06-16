from graphics import *
import time

class Ball:
    def __init__(self, win, x, y, radius, color):
        self.win = win
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = 0
        self.gravity = -9.8
        self.bounce_factor = 0.60

        self.shape = Circle(Point(x, y), radius)
        self.shape.setFill(color)
        self.shape.draw(win)

    def update(self, dt):
        old_y = self.y

        self.velocity = self.velocity + self.gravity * dt
        self.y = self.y + self.velocity * dt

        if self.y <= self.radius:
            self.y = self.radius
            self.velocity = -self.velocity * self.bounce_factor

        dy = self.y - old_y
        self.shape.move(0, dy)

    def still_bouncing(self):
        return abs(self.velocity) > 0.1 or self.y > self.radius + 0.1

def main():
    height = float(input("Enter starting height in meters: "))

    win = GraphWin("Physics Bouncing Balls", 500, 500)
    win.setCoords(0, 0, 10, 10)

    balls = [
        Ball(win, 3, height, 0.3, "red"),
        Ball(win, 5, height * 0.8, 0.3, "blue"),
        Ball(win, 7, height * 0.6, 0.3, "green")
    ]

    dt = 0.05

    running = True

    while running:
        running = False

        for ball in balls:
            ball.update(dt)

            if ball.still_bouncing():
                running = True

        time.sleep(dt)

    message = Text(Point(5, 9), "Done bouncing. Click to exit.")
    message.draw(win)

    win.getMouse()
    win.close()

main()
