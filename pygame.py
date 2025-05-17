import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Free Fire Head Shot Panel")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the font
font = pygame.font.SysFont("Arial", 30)

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Set up the enemies
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 5

# Set up the score
score = 0

# Set up the game over flag
game_over = False

# Set up the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0
        score += 1

    # Check for collision
    if (player_x < enemy_x + enemy_width and
        player_x + player_width > enemy_x and
        player_y < enemy_y + enemy_height and
        player_y + player_height > enemy_y):
        game_over = True

    # Draw the screen
    screen.fill(black)
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    # Update the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()