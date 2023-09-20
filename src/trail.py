import pygame

points = []
max_points = 20
line_width = 5

def trail(screen, pressed, mouse_pos):
    global points
    if not pressed:
        if len(points) > 0:
            pygame.time.wait(5)
            points.pop(0)
    if pressed:
        points.append(mouse_pos)
        if len(points) > max_points:
            points.pop(0)
    if len(points) > 1:
        for i in range(1, len(points)):
            pygame.draw.line(screen, (18, 105, 232), points[i-1], points[i], line_width)

