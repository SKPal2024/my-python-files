import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)

    def change_direction(self, dx, dy):
        self.direction = (dx, dy)

    def check_collision(self):
        head_x, head_y = self.body[0]
        return (
            head_x < 0
            or head_x >= GRID_WIDTH
            or head_y < 0
            or head_y >= GRID_HEIGHT
            or len(self.body) != len(set(self.body))
        )

    def grow(self):
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

# Food class
class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

# Initialize game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
snake = Snake()
food = Food()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -1)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, 1)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(1, 0)

    snake.move()

    if snake.check_collision():
        print("Game over!")
        pygame.quit()
        sys.exit()

    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.random_position()

    # Draw everything
    screen.fill(WHITE)
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, GREEN, (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.display.flip()

    pygame.time.Clock().tick(10)  # Control snake speed

# Clean up
pygame.quit()
