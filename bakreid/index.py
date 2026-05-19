import pygame
import sys
import random

# ---------------------------------------------------
# Initialize Pygame
# ---------------------------------------------------
pygame.init()
pygame.font.init()

# ---------------------------------------------------
# Screen setup
# ---------------------------------------------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eid-ul-Adha Mubarak")
clock = pygame.time.Clock()

# ---------------------------------------------------
# Colors
# ---------------------------------------------------
WHITE = (255, 255, 255)
SKY = (10, 10, 40)
YELLOW = (255, 215, 0)
GREEN = (20, 120, 40)
BROWN = (139, 69, 19)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)

# ---------------------------------------------------
# Safe Fonts (works in browser + desktop)
# ---------------------------------------------------
title_font = pygame.font.Font(None, 72)
subtitle_font = pygame.font.Font(None, 56)

# ---------------------------------------------------
# Stars
# ---------------------------------------------------
stars = [
    (
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT // 2),
        random.randint(1, 3)
    )
    for _ in range(80)
]

# ---------------------------------------------------
# Goat Drawing
# ---------------------------------------------------
def create_goat():
    goat = pygame.Surface((140, 100), pygame.SRCALPHA)

    # Body
    pygame.draw.ellipse(goat, GRAY, (40, 35, 75, 45))

    # Head
    pygame.draw.ellipse(goat, (235, 235, 235), (5, 25, 55, 45))

    # Legs
    for x in [55, 75, 95, 110]:
        pygame.draw.rect(goat, (190, 190, 190), (x, 72, 8, 22))

    # Eyes
    pygame.draw.circle(goat, WHITE, (25, 45), 6)
    pygame.draw.circle(goat, WHITE, (42, 45), 6)
    pygame.draw.circle(goat, BLACK, (25, 45), 2)
    pygame.draw.circle(goat, BLACK, (42, 45), 2)

    # Horns
    pygame.draw.arc(goat, BROWN, (0, 0, 25, 35), 3.1, 5.2, 4)
    pygame.draw.arc(goat, BROWN, (35, 0, 25, 35), 3.1, 5.2, 4)

    # Tail
    pygame.draw.line(goat, BLACK, (112, 50), (128, 40), 3)

    return goat


# ---------------------------------------------------
# Moon
# ---------------------------------------------------
def create_moon():
    moon = pygame.Surface((120, 120), pygame.SRCALPHA)
    pygame.draw.circle(moon, YELLOW, (60, 60), 45)
    pygame.draw.circle(moon, SKY, (78, 55), 40)
    return moon


# ---------------------------------------------------
# Cloud
# ---------------------------------------------------
def create_cloud():
    cloud = pygame.Surface((140, 70), pygame.SRCALPHA)
    pygame.draw.ellipse(cloud, WHITE, (0, 25, 140, 35))
    pygame.draw.ellipse(cloud, WHITE, (20, 0, 90, 60))
    pygame.draw.ellipse(cloud, WHITE, (60, 10, 70, 50))
    return cloud


# ---------------------------------------------------
# Mosque
# ---------------------------------------------------
def draw_mosque():
    # Main building
    pygame.draw.rect(screen, (25, 25, 25), (250, 350, 400, 180))

    # Dome
    pygame.draw.circle(screen, (40, 40, 40), (450, 330), 80)

    # Minarets
    pygame.draw.rect(screen, (30, 30, 30), (200, 260, 40, 270))
    pygame.draw.rect(screen, (30, 30, 30), (660, 260, 40, 270))

    pygame.draw.polygon(
        screen,
        (50, 50, 50),
        [(200, 260), (220, 210), (240, 260)]
    )

    pygame.draw.polygon(
        screen,
        (50, 50, 50),
        [(660, 260), (680, 210), (700, 260)]
    )


# ---------------------------------------------------
# Create Assets
# ---------------------------------------------------
goat_img = create_goat()
moon_img = create_moon()
cloud_img = create_cloud()

# ---------------------------------------------------
# Animation Variables
# ---------------------------------------------------
goat_x1 = -150
goat_x2 = WIDTH + 150
cloud_x = 0

# ---------------------------------------------------
# Main Function
# ---------------------------------------------------
def main():
    global goat_x1, goat_x2, cloud_x

    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Background
        screen.fill(SKY)

        # Stars
        for x, y, size in stars:
            pygame.draw.circle(screen, WHITE, (x, y), size)

        # Moon
        screen.blit(moon_img, (WIDTH // 2 - 60, 40))

        # Clouds
        cloud_x -= 0.4
        if cloud_x < -200:
            cloud_x = WIDTH

        screen.blit(cloud_img, (cloud_x, 100))
        screen.blit(cloud_img, (cloud_x + 280, 150))
        screen.blit(cloud_img, (cloud_x + 550, 110))

        # Mosque
        draw_mosque()

        # Ground
        pygame.draw.rect(screen, GREEN, (0, HEIGHT - 100, WIDTH, 100))

        # Goat movement
        goat_x1 += 1
        goat_x2 -= 1

        if goat_x1 > WIDTH + 50:
            goat_x1 = -150

        if goat_x2 < -150:
            goat_x2 = WIDTH + 150

        screen.blit(goat_img, (goat_x1, HEIGHT - 165))
        screen.blit(goat_img, (goat_x2, HEIGHT - 165))

        # Text Shadow
        shadow1 = title_font.render("Eid-ul-Adha", True, BLACK)
        shadow2 = subtitle_font.render("Mubarak", True, BLACK)

        screen.blit(
            shadow1,
            (
                WIDTH // 2 - shadow1.get_width() // 2 + 3,
                420 + 3
            )
        )
        screen.blit(
            shadow2,
            (
                WIDTH // 2 - shadow2.get_width() // 2 + 3,
                490 + 3
            )
        )

        # Main Text
        title = title_font.render("Eid-ul-Adha", True, YELLOW)
        subtitle = subtitle_font.render("Mubarak", True, WHITE)

        screen.blit(
            title,
            (
                WIDTH // 2 - title.get_width() // 2,
                420
            )
        )
        screen.blit(
            subtitle,
            (
                WIDTH // 2 - subtitle.get_width() // 2,
                490
            )
        )

        # Update screen
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# ---------------------------------------------------
# Run Program
# ---------------------------------------------------
if __name__ == "__main__":
    main()
